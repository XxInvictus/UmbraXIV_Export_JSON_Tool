import argparse
import base64
import csv
import difflib
import json
import logging
import sys
import zlib

import requests

logging.basicConfig(level=logging.INFO)
verbose_enabled = False

# Validate the string is an UmbraXIV Widget Import string and extract the encoded string
def validate_and_extract_encoded_string(input_string: str) -> str:
    try:
        separated_input = input_string.split('|')
        if len(separated_input) < 3:
            raise ValueError("Input string is not formatted correctly.")
        elif separated_input[0] != 'WI':
            raise ValueError("Input string is not an UmbraXIV Widget Import string.")
        elif separated_input[1] != 'ShortcutPanel':
            raise ValueError("Import string is not a Shortcut Panel")
        return separated_input[2]
    except Exception as e:
        logging.error(f"Error validating and preparing input: {e}")
        raise


# Prefix the encoded string and return an UmbraXIV Widget Import string
def prefix_encoded_string_for_import(encoded_string: str) -> str:
    try:
        return f"WI|ShortcutPanel|{encoded_string}"
    except Exception as e:
        logging.error(f"Error prefixing encoded string: {e}")
        raise


# Decode a base64 encoded string
def decode_base64(encoded_string: str) -> bytes:
    try:
        return base64.b64decode(encoded_string)
    except Exception as e:
        logging.error(f"Error decoding base64: {e}")
        raise


# Parse a JSON object from a decoded byte string
def parse_json(decoded_bytes: bytes) -> dict:
    try:
        return json.loads(decoded_bytes)
    except Exception as e:
        logging.error(f"Error parsing JSON: {e}")
        raise


# Sort a JSON object by key
def sort_json(json_data: dict) -> dict:
    try:
        return {k: json_data[k] for k in sorted(json_data, key=int)}
    except Exception as e:
        logging.error(f"Error sorting JSON: {e}")
        raise


# Decompress a zlib compressed byte string
def decompress_zlib(encoded_data: bytes) -> bytes:
    try:
        return zlib.decompress(encoded_data, -zlib.MAX_WBITS)
    except Exception as e:
        logging.error(f"Error decompressing zlib: {e}")
        raise


# Encode a byte string to base64
def encode_base64(data: bytes) -> str:
    try:
        return base64.b64encode(data).decode('ascii')
    except Exception as e:
        logging.error(f"Error encoding base64: {e}")
        raise


# Serialize a dictionary to JSON
def serialize_json(data: dict) -> str:
    try:
        return json.dumps(data)
    except Exception as e:
        logging.error(f"Error serializing JSON: {e}")
        raise


# Compress a byte string with zlib
def compress_zlib(data: bytes) -> bytes:
    try:
        return zlib.compress(data, level=zlib.Z_BEST_COMPRESSION, wbits=-zlib.MAX_WBITS)
    except Exception as e:
        logging.error(f"Error compressing zlib: {e}")
        raise


# Get data from a URL
def get_data_from_url(url):
    request_data = requests.get(url)
    if request_data.status_code == 200:
        data = request_data.content.decode('utf-8-sig')
        return data.splitlines()
    sys.exit(f"{url} not available")


# Create a dictionary from a CSV file
def dict_from_csv(csv_data: list[str]) -> dict:
    data = {}
    csv_reader = csv.DictReader([csv_data[1]] + csv_data[3:])

    for rows in csv_reader:
        cleaned_dict = {
            "Name": rows["Name"],
            "Icon": rows["Icon"]
        }
        key = rows['#']
        data[key] = cleaned_dict

    return data


# Lookup an emote ID in a dictionary and return the emote name
def lookup_emote_id_to_name(emote_id: int, emote_dict: dict) -> str:
    try:
        return emote_dict[str(emote_id)]["Name"]
    except Exception as e:
        logging.error(f"Error converting emote ID to name: {e}")
        raise


# Translate emote IDs to names in an UmbraXIV Shortcut Panel
def translate_emote_ids_to_names(shortcut_panel: dict) -> dict:
    try:
        emote_data = get_data_from_url("https://github.com/xivapi/ffxiv-datamining/raw/master/csv/Emote.csv")
        emote_dict = dict_from_csv(emote_data)
        for tab in shortcut_panel:
            for slot in shortcut_panel[tab]:
                split_slot = shortcut_panel[tab][slot].split('/')
                if len(split_slot) == 2 and split_slot[0] == 'EM':
                    shortcut_panel[tab][
                        slot] = f"{split_slot[0]}/{lookup_emote_id_to_name(int(split_slot[1]), emote_dict)}"
        return shortcut_panel
    except Exception as e:
        logging.error(f"Error translating emote IDs to names: {e}")
        raise


# Lookup an emote name in a dictionary and return the emote ID
def lookup_emote_name_to_id(emote_name: str, emote_dict: dict) -> int:
    try:
        for emote_id, emote_data in emote_dict.items():
            if emote_data["Name"] == emote_name:
                return int(emote_id)
        raise ValueError("Emote name not found in emote dictionary.")
    except Exception as e:
        logging.error(f"Error converting emote name to ID: {e}")
        raise


# Translate emote names to IDs in an UmbraXIV Shortcut Panel
def translate_emote_names_to_ids(shortcut_panel: dict) -> dict:
    try:
        emote_data = get_data_from_url("https://github.com/xivapi/ffxiv-datamining/raw/master/csv/Emote.csv")
        emote_dict = dict_from_csv(emote_data)
        for tab in shortcut_panel:
            for slot in shortcut_panel[tab]:
                split_slot = shortcut_panel[tab][slot].split('/')
                if len(split_slot) == 2 and split_slot[0] == 'EM':
                    shortcut_panel[tab][slot] = f"{split_slot[0]}/{lookup_emote_name_to_id(split_slot[1], emote_dict)}"
        return shortcut_panel
    except Exception as e:
        logging.error(f"Error translating emote names to IDs: {e}")
        raise


# Main decode function
def decode(exported_string: str, output_file: str = None, convert_emotes: bool = False):
    try:
        encoded_string = validate_and_extract_encoded_string(exported_string)
        decoded_bytes = decode_base64(encoded_string)
        decoded_json = parse_json(decoded_bytes)
        shortcut_panel = decoded_json['SlotConfig']
        split_shortcut_panel = shortcut_panel.split('|')
        if split_shortcut_panel[0] == 'SPD':
            encoded_shortcut_panel = split_shortcut_panel[1]
            decoded_shortcut_panel = decode_base64(encoded_shortcut_panel)
            inflated_shortcut_panel = decompress_zlib(decoded_shortcut_panel)
            decoded_json['SlotConfig'] = parse_json(inflated_shortcut_panel)
            decoded_json['SlotConfig'] = sort_json(decoded_json['SlotConfig'])
            for tab in decoded_json['SlotConfig']:
                decoded_json['SlotConfig'][tab] = sort_json(decoded_json['SlotConfig'][tab])
            if convert_emotes:
                decoded_json['SlotConfig'] = translate_emote_ids_to_names(decoded_json['SlotConfig'])
        json_result = json.dumps(decoded_json, indent=4)
        if output_file:
            with open(output_file, 'w') as file:
                file.write(json_result)
            return f"Output written to {output_file}"
        else:
            return json_result
    except Exception as e:
        logging.error(f"Error in decode function: {e}")


# Main encode function
def encode(input_json: dict, output_file: str = None, convert_emotes: bool = False):
    try:
        if input_json["SlotConfig"]:
            if convert_emotes:
                input_json["SlotConfig"] = translate_emote_names_to_ids(input_json["SlotConfig"])
            serialized_shortcut_panel = serialize_json(input_json["SlotConfig"])
            deflated_shortcut_panel = compress_zlib(serialized_shortcut_panel.encode('utf-8'))
            encoded_shortcut_panel = encode_base64(deflated_shortcut_panel)
            input_json["SlotConfig"] = f"SPD|{encoded_shortcut_panel}"
        serialized_json = serialize_json(input_json)
        encoded_string = encode_base64(serialized_json.encode('utf-8'))
        import_string = prefix_encoded_string_for_import(encoded_string)
        if output_file:
            with open(output_file, 'w') as file:
                file.write(import_string)
            return f"Output written to {output_file}"
        else:
            print(import_string)
            return import_string
    except Exception as e:
        logging.error(f"Error in encode function: {e}")


# Test the encode and decode functions with a known working string ensuring the re-encoded string matches the original encoded string
def test_encode_decode():
    # This string was generated and test imported into UmbraXIV
    # A string directly exported from UmbraXIV will not work here due to differences in C and Python zlib compression defaults
    original_encoded_string = "WI|ShortcutPanel|eyJCdXR0b25MYWJlbCI6ICJFbW90ZSBNZW51IiwgIkJ1dHRvbkljb25JZCI6IDAsICJEZWNvcmF0ZSI6IHRydWUsICJEZXNhdHVyYXRlSWNvbiI6IGZhbHNlLCAiRGlzcGxheU1vZGUiOiAiVGV4dEFuZEljb24iLCAiSWNvbkxvY2F0aW9uIjogIkxlZnQiLCAiSWNvbkNvbG9yIjogNDI5NDk2NzI5NSwgIlRleHRBbGlnbiI6ICJMZWZ0IiwgIkljb25TaXplIjogMCwgIkljb25ZT2Zmc2V0IjogMCwgIkxhYmVsTWF4V2lkdGgiOiAwLCAiVGV4dFlPZmZzZXQiOiAwLCAiQ2F0ZWdvcnlOYW1lXzAiOiAiU2hvcnRjdXQgUGFuZWwiLCAiQ2F0ZWdvcnlOYW1lXzEiOiAiIiwgIkNhdGVnb3J5TmFtZV8yIjogIiIsICJDYXRlZ29yeU5hbWVfMyI6ICIiLCAiTnVtQ29scyI6IDE2LCAiTnVtUm93cyI6IDE2LCAiU2hvd0VtcHR5U2xvdHMiOiBmYWxzZSwgIlNsb3RDb25maWciOiAiU1BEfFhWWkxqbHd4Q0x6S3FOZVJZakQ0ay8wc2M2TFIzRDE2RkJTZDJiU0ViWXJpVjYrL1h1UDE1K01yZmwrZmYzL2JldjM2ZUltbnFXR3R1bnlzcVhWM0g5TjJtakwzWSsreVZlUDVQclJ4ZjJuN1l4K0dpdXRUc2ZROHBzNnk1VXdjTUo0ckRpckFnVDM0WU1GakVISXVIREJrQmhtV0Izc0FzamhtVEsrVU4wTDRUSHZCMzh0ZkxnQzhJbXdCb0pOVFBwQjZrRm1SQVNoNjllTkVFZFhLbGdFSEt3QVZlRmh4RklTMHlRY2dyU1E1Z0tra2RRQ2hyUFVBaHJLVUVvbktaUkNVVXU3a0FVYmxFbU1hRG5vK0JnNnFYK2lmY0VBYzl6MGdGaXprREI3QTQzVHVqZ09PSktvakhFSzVzSnNWR240NFJEa1NGWFNoTnNKNk8xb3NGWE01N0FxNU5nRG9VQWlzek5uSSsvSkZRckFoRG96ZU9rVWFWaStRcHJGaG5qRTQyWW9lU3k4SDVzd3E2RVlockR3Y3RuWWhZSk1rUmwyNEd2TWl6NnFER0RqT1Rod1Jpb0lING02S2NYODd4K2p1TmJZdS9ZdlJSUGY1UU9xQVZaZ1JnU09vSXloelJuVmphQW1BWldSamRDSUQvV0ZYaG9ZU1ZYNDVXUVVHK3BPakdGeTZHQ2ovZVpkUlpoYTRzMmhFNzlrbmhXUHZRSmpVVkV3cnB4bTd6akdSZU0wZUc2RDlQeXpxQWhhV3NvSGtLMjRxWmJsYXNLTG16Q2pzNGV6Z21yZmd6QjNGaXBKRUlKTkVhZ0ozSlM3WllVZ1h4ZEhpbXRvb0tEcTE5QkgyaDJhOXpsM25hNEJ4SUNHMTFIYUl5NC9RV3RpUWdmNzRvTlQ4RUVTU3JIdXFaeWxFZUhheE1PZURjUU9wUlM3aVV1SUVpMHFGa3hYdWgwTU1BVHRjMCtqNW13cUhPMFZZc1VTdHdSR2MwcFM2UXpFenFBS1hIaHQzV2wzUjNNRXlZT2tQKzRtbFp1NVFRbjdNZHVvYWsxM0E0MUR1ZE9DdTRKdmlSU0EzM0x1NEFIQit3REZmUGFxNTQ4M3c1R2VxT0Mxcy9XMU9LWVJjSTBtSS9zQUM0clNVQmUyM2Z3VVEvTDYzMS9mM1B3PT0iLCAiX0VuYWJsZWQiOiB0cnVlLCAiQnV0dG9uUGFkZGluZyI6IDAsICJNYXhUZXh0V2lkdGgiOiAwLCAiVGV4dFNpemUiOiAxMywgIkF1dG9DbG9zZU9uVXNlIjogdHJ1ZX0="

    # Decode the original encoded string
    try:
        decoded_json = decode(original_encoded_string)
    except Exception as e:
        print(f"Decoding failed: {e}")
        return

    # Re-encode the decoded JSON
    try:
        re_encoded_string = encode(json.loads(decoded_json))
    except Exception as e:
        print(f"Encoding failed: {e}")
        return

    # Compare the re-encoded string to the original encoded string
    if re_encoded_string == original_encoded_string:
        return "Test passed: The re-encoded string matches the original encoded string."
    else:
        diff = difflib.unified_diff(
            original_encoded_string.splitlines(),
            re_encoded_string.splitlines(),
            fromfile='original',
            tofile='re-encoded',
            lineterm=''
        )
        for line in diff:
            print(line)
        print(difflib.SequenceMatcher(None, original_encoded_string, re_encoded_string).ratio())
        return "Test failed: The re-encoded string does not match the original encoded string."


# Main function
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Encode or Decode an UmbraXIV Shortcut Panel to or from JSON')
        parser.add_argument('-s', '--input_string', type=str, help='The input string to encode/decode')
        parser.add_argument('-f', '--input_file', type=str, help='The input file to encode/decode')
        parser.add_argument('-o', '--output_file', type=str, help='The output file to write the result')
        parser.add_argument('-d', '--decode', action='store_true', help='Decode the input string')
        parser.add_argument('-e', '--encode', action='store_true', help='Encode the input JSON')
        parser.add_argument('-c', '--convert', action='store_true', help='Convert emote IDs to names or names to IDs')
        parser.add_argument('-t', '--test', action='store_true',
                            help='Test the encode and decode functions with a known string')
        parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Enable verbose logging')
        parser.add_argument('unknown', nargs='*', help=argparse.SUPPRESS)
        args, unknown_args = parser.parse_known_args()
        verbose_enabled = args.verbose

        # Check for unexpected arguments and exit if found
        if any([args.unknown, unknown_args]) and args.unknown :
            print(f"Unknown arguments: {unknown_args} {args.unknown}")
            parser.print_help()
            sys.exit(1)

        # Check for required inputs and exit if not found
        if not any([args.input_string, args.input_file, args.test]):
            print("Error: You must provide either an input string or an input file.")
            parser.print_help()
            sys.exit(1)

        # Check for required actions and exit if not found
        if not any([args.decode, args.encode, args.test]):
            print("Error: You must provide either the encode or decode argument.")
            parser.print_help()
            sys.exit(1)

        # Check if both encode and decode arguments are used and exit if found
        if all([args.decode, args.encode]):
            print("Error: You cannot use both the encode and decode arguments.")
            parser.print_help()
            sys.exit(1)

        # Check if the test argument is used with other arguments and exit if found
        if args.test and any([args.input_string, args.input_file, args.decode, args.encode, args.convert]):
            print("Error: The test argument cannot be used with other arguments.")
            parser.print_help()
            sys.exit(1)

        if args.decode:
            if args.input_file:
                with open(args.input_file, 'r') as file:
                    input_string = file.read()
            else:
                input_string = args.input_string
            output_result = decode(input_string, args.output_file, args.convert)
        elif args.encode:
            if args.input_file:
                with open(args.input_file, 'r') as file:
                    input_json = json.load(file)
            else:
                input_json = json.loads(args.input_string)
            output_result = encode(input_json, args.output_file, args.convert)
        elif args.test:
            output_result = test_encode_decode()
        else:
            parser.print_help()
            sys.exit(0)
        print(output_result)
    except BaseException:
        # Ensures the console window does not close immediately on error or completion
         if verbose_enabled:
            print(sys.exc_info()[0])
            import traceback
            print(traceback.format_exc())
    finally:
        input("Press Enter to close the window...")
