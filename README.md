# UmbraXIV_Export_JSON_Tool
Tool for encoding/decoding UmbraXIV exports to/from JSON

## Features
- **_Currently only supports Umbra XIV Shortcut Panels, may expand on this later_**
- Convert UmbraXIV Shortcut Panel export to JSON
- Convert JSON to UmbraXIV Shortcut Panel export
- Convert Emotes between IDs and Names when Converting to/from JSON
- Output either to file or console

## Installation
- **_Requires Python 3.6+_**
- Clone the repository
- Install the required packages with `pip install -r requirements.txt`
- Run the script using the usage instructions below or `python umbraxiv_export_json_tool.py` without arguments to view the help

## Usage
_In all examples below replace values in `{}` with your own values_

<details>
<summary>Click to Expand in-built Help</summary>

```shell
usage: umbraxiv_export_json_tool.py [-h] [-s INPUT_STRING] [-f INPUT_FILE] [-o OUTPUT_FILE] [-d] [-e] [-c] [-t] [-v]

Encode or Decode an UmbraXIV Shortcut Panel to or from JSON

options:
  -h, --help            show this help message and exit
  -s INPUT_STRING, --input_string INPUT_STRING
                        The input string to encode/decode
  -f INPUT_FILE, --input_file INPUT_FILE
                        The input file to encode/decode
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        The output file to write the result
  -d, --decode          Decode the input string
  -e, --encode          Encode the input JSON
  -c, --convert         Convert emote IDs to names or names to IDs
  -t, --test            Test the encode and decode functions with a known string
  -v, --verbose         Enable verbose logging
Press Enter to close the window...
```

</details>

### UmbraXIV encoded export as CLI argument with JSON output to console
```shell
python umbraxiv_export_json_tool.py -d -s "{UmbraXIV_Export_String}"
```
#### Example:
```shell
python umbraxiv_export_json_tool.py -d -s "WI|ShortcutPanel|eyJCdXR0b25MYWJlbCI6ICJFbW90ZSBNZW51IiwgIkJ1dHRvbkljb25JZCI6IDAsICJEZWNvcmF0ZSI6IHRydWUsICJEZXNhdHVyYXRlSWNvbiI6IGZhbHNlLCAiRGlzcGxheU1vZGUiOiAiVGV4dEFuZEljb24iLCAiSWNvbkxvY2F0aW9uIjogIkxlZnQiLCAiSWNvbkNvbG9yIjogNDI5NDk2NzI5NSwgIlRleHRBbGlnbiI6ICJMZWZ0IiwgIkljb25TaXplIjogMCwgIkljb25ZT2Zmc2V0IjogMCwgIkxhYmVsTWF4V2lkdGgiOiAwLCAiVGV4dFlPZmZzZXQiOiAwLCAiQ2F0ZWdvcnlOYW1lXzAiOiAiU2hvcnRjdXQgUGFuZWwiLCAiQ2F0ZWdvcnlOYW1lXzEiOiAiIiwgIkNhdGVnb3J5TmFtZV8yIjogIiIsICJDYXRlZ29yeU5hbWVfMyI6ICIiLCAiTnVtQ29scyI6IDE2LCAiTnVtUm93cyI6IDE2LCAiU2hvd0VtcHR5U2xvdHMiOiBmYWxzZSwgIlNsb3RDb25maWciOiAiU1BEfFhWWkxqbHd4Q0x6S3FOZVJZakQ0ay8wc2M2TFIzRDE2RkJTZDJiU0ViWXJpVjYrL1h1UDE1K01yZmwrZmYzL2JldjM2ZUltbnFXR3R1bnlzcVhWM0g5TjJtakwzWSsreVZlUDVQclJ4ZjJuN1l4K0dpdXRUc2ZROHBzNnk1VXdjTUo0ckRpckFnVDM0WU1GakVISXVIREJrQmhtV0Izc0FzamhtVEsrVU4wTDRUSHZCMzh0ZkxnQzhJbXdCb0pOVFBwQjZrRm1SQVNoNjllTkVFZFhLbGdFSEt3QVZlRmh4RklTMHlRY2dyU1E1Z0tra2RRQ2hyUFVBaHJLVUVvbktaUkNVVXU3a0FVYmxFbU1hRG5vK0JnNnFYK2lmY0VBYzl6MGdGaXprREI3QTQzVHVqZ09PSktvakhFSzVzSnNWR240NFJEa1NGWFNoTnNKNk8xb3NGWE01N0FxNU5nRG9VQWlzek5uSSsvSkZRckFoRG96ZU9rVWFWaStRcHJGaG5qRTQyWW9lU3k4SDVzd3E2RVlockR3Y3RuWWhZSk1rUmwyNEd2TWl6NnFER0RqT1Rod1Jpb0lING02S2NYODd4K2p1TmJZdS9ZdlJSUGY1UU9xQVZaZ1JnU09vSXloelJuVmphQW1BWldSamRDSUQvV0ZYaG9ZU1ZYNDVXUVVHK3BPakdGeTZHQ2ovZVpkUlpoYTRzMmhFNzlrbmhXUHZRSmpVVkV3cnB4bTd6akdSZU0wZUc2RDlQeXpxQWhhV3NvSGtLMjRxWmJsYXNLTG16Q2pzNGV6Z21yZmd6QjNGaXBKRUlKTkVhZ0ozSlM3WllVZ1h4ZEhpbXRvb0tEcTE5QkgyaDJhOXpsM25hNEJ4SUNHMTFIYUl5NC9RV3RpUWdmNzRvTlQ4RUVTU3JIdXFaeWxFZUhheE1PZURjUU9wUlM3aVV1SUVpMHFGa3hYdWgwTU1BVHRjMCtqNW13cUhPMFZZc1VTdHdSR2MwcFM2UXpFenFBS1hIaHQzV2wzUjNNRXlZT2tQKzRtbFp1NVFRbjdNZHVvYWsxM0E0MUR1ZE9DdTRKdmlSU0EzM0x1NEFIQit3REZmUGFxNTQ4M3c1R2VxT0Mxcy9XMU9LWVJjSTBtSS9zQUM0clNVQmUyM2Z3VVEvTDYzMS9mM1B3PT0iLCAiX0VuYWJsZWQiOiB0cnVlLCAiQnV0dG9uUGFkZGluZyI6IDAsICJNYXhUZXh0V2lkdGgiOiAwLCAiVGV4dFNpemUiOiAxMywgIkF1dG9DbG9zZU9uVXNlIjogdHJ1ZX0="
```
#### Output:
<details>
<summary>Click to Expand</summary>

```shell
{
    "ButtonLabel": "Emote Menu",
    "ButtonIconId": 0,
    "Decorate": true,
    "DesaturateIcon": false,
    "DisplayMode": "TextAndIcon",
    "IconLocation": "Left",
    "IconColor": 4294967295,
    "TextAlign": "Left",
    "IconSize": 0,
    "IconYOffset": 0,
    "LabelMaxWidth": 0,
    "TextYOffset": 0,
    "CategoryName_0": "Shortcut Panel",
    "CategoryName_1": "",
    "CategoryName_2": "",
    "CategoryName_3": "",
    "NumCols": 16,
    "NumRows": 16,
    "ShowEmptySlots": false,
    "SlotConfig": {
        "0": {
            "0": "EM/46",
            "1": "EM/34",
            "2": "EM/21",
            "3": "EM/30",
            "4": "EM/43",
            "5": "EM/112",
            "6": "EM/41",
            "8": "EM/17",
            "9": "EM/36",
            "10": "EM/3",
            "11": "EM/49",
            "12": "EM/233",
            "13": "EM/233",
            "14": "EM/171",
            "15": "EM/2",
            "16": "EM/4",
            "17": "EM/121",
            "18": "EM/246",
            "19": "EM/18",
            "20": "EM/122",
            "21": "EM/58",
            "22": "EM/6",
            "24": "EM/204",
            "25": "EM/40",
            "26": "EM/111",
            "27": "EM/26",
            "28": "EM/2",
            "29": "EM/24",
            "30": "EM/10",
            "31": "EM/25",
            "32": "EM/29",
            "33": "EM/7",
            "34": "EM/48",
            "35": "EM/112",
            "36": "EM/276",
            "37": "EM/114",
            "38": "EM/146",
            "41": "EM/38",
            "42": "EM/33",
            "43": "EM/32",
            "44": "EM/14",
            "45": "EM/24",
            "46": "EM/47",
            "47": "EM/137",
            "48": "EM/9",
            "49": "EM/20",
            "50": "EM/125",
            "51": "EM/205",
            "52": "EM/42",
            "53": "EM/1",
            "54": "EM/195",
            "76": "EM/226",
            "77": "EM/224",
            "78": "EM/227",
            "79": "EM/225",
            "80": "EM/22",
            "81": "EM/159",
            "82": "EM/166",
            "83": "EM/256",
            "84": "EM/37",
            "85": "EM/27",
            "86": "EM/28",
            "87": "EM/191",
            "88": "EM/140",
            "89": "EM/106",
            "92": "EM/278",
            "93": "EM/202",
            "94": "EM/206",
            "95": "EM/221",
            "96": "EM/139",
            "97": "EM/231",
            "98": "EM/54",
            "99": "EM/23",
            "100": "EM/45",
            "101": "EM/35",
            "102": "EM/44",
            "103": "EM/155",
            "104": "EM/39",
            "105": "EM/213",
            "128": "EM/15",
            "129": "EM/172",
            "130": "EM/16",
            "140": "EM/75",
            "141": "EM/161",
            "142": "EM/77",
            "143": "EM/74",
            "144": "EM/5",
            "145": "EM/154",
            "146": "EM/59",
            "147": "EM/55",
            "148": "EM/31",
            "157": "EM/78",
            "158": "EM/141",
            "159": "EM/80",
            "176": "EM/13",
            "177": "EM/19",
            "178": "EM/50",
            "179": "EM/241",
            "180": "EM/242",
            "181": "EM/215",
            "182": "EM/203",
            "183": "EM/214",
            "184": "EM/207",
            "188": "EM/133",
            "189": "EM/184",
            "190": "EM/69",
            "191": "EM/162",
            "192": "EM/136",
            "193": "EM/132",
            "194": "EM/131",
            "195": "EM/135",
            "196": "EM/134",
            "197": "EM/130",
            "198": "EM/52",
            "199": "EM/165",
            "200": "EM/164",
            "201": "EM/143",
            "204": "EM/70",
            "205": "EM/228",
            "206": "EM/236",
            "207": "EM/163",
            "208": "EM/156",
            "209": "EM/64",
            "210": "EM/158",
            "211": "EM/65",
            "212": "EM/67",
            "213": "EM/187",
            "214": "EM/157",
            "215": "EM/223",
            "216": "EM/222",
            "217": "EM/150",
            "224": "EM/104",
            "225": "EM/186",
            "226": "EM/101",
            "227": "EM/118",
            "234": "EM/76",
            "235": "EM/160",
            "236": "EM/183",
            "237": "EM/152",
            "238": "EM/82",
            "239": "EM/83",
            "240": "EM/103",
            "241": "EM/216",
            "242": "EM/11",
            "243": "EM/212",
            "249": "EM/79",
            "250": "EM/84",
            "251": "EM/73",
            "252": "EM/72",
            "253": "EM/68",
            "254": "EM/190",
            "255": "EM/71"
        }
    },
    "_Enabled": true,
    "ButtonPadding": 0,
    "MaxTextWidth": 0,
    "TextSize": 13,
    "AutoCloseOnUse": true
}
Press Enter to close the window...
```

</details>

### UmbraXIV encoded export as CLI argument with JSON output to file
```shell
python umbraxiv_export_json_tool.py -d -s "{UmbraXIV_Export_String}" -o "{Output_File_Path}"
```
#### Example:
```shell
python umbraxiv_export_json_tool.py -d -s "WI|ShortcutPanel|eyJCdXR0b25MYWJlbCI6ICJFbW90ZSBNZW51IiwgIkJ1dHRvbkljb25JZCI6IDAsICJEZWNvcmF0ZSI6IHRydWUsICJEZXNhdHVyYXRlSWNvbiI6IGZhbHNlLCAiRGlzcGxheU1vZGUiOiAiVGV4dEFuZEljb24iLCAiSWNvbkxvY2F0aW9uIjogIkxlZnQiLCAiSWNvbkNvbG9yIjogNDI5NDk2NzI5NSwgIlRleHRBbGlnbiI6ICJMZWZ0IiwgIkljb25TaXplIjogMCwgIkljb25ZT2Zmc2V0IjogMCwgIkxhYmVsTWF4V2lkdGgiOiAwLCAiVGV4dFlPZmZzZXQiOiAwLCAiQ2F0ZWdvcnlOYW1lXzAiOiAiU2hvcnRjdXQgUGFuZWwiLCAiQ2F0ZWdvcnlOYW1lXzEiOiAiIiwgIkNhdGVnb3J5TmFtZV8yIjogIiIsICJDYXRlZ29yeU5hbWVfMyI6ICIiLCAiTnVtQ29scyI6IDE2LCAiTnVtUm93cyI6IDE2LCAiU2hvd0VtcHR5U2xvdHMiOiBmYWxzZSwgIlNsb3RDb25maWciOiAiU1BEfFhWWkxqbHd4Q0x6S3FOZVJZakQ0ay8wc2M2TFIzRDE2RkJTZDJiU0ViWXJpVjYrL1h1UDE1K01yZmwrZmYzL2JldjM2ZUltbnFXR3R1bnlzcVhWM0g5TjJtakwzWSsreVZlUDVQclJ4ZjJuN1l4K0dpdXRUc2ZROHBzNnk1VXdjTUo0ckRpckFnVDM0WU1GakVISXVIREJrQmhtV0Izc0FzamhtVEsrVU4wTDRUSHZCMzh0ZkxnQzhJbXdCb0pOVFBwQjZrRm1SQVNoNjllTkVFZFhLbGdFSEt3QVZlRmh4RklTMHlRY2dyU1E1Z0tra2RRQ2hyUFVBaHJLVUVvbktaUkNVVXU3a0FVYmxFbU1hRG5vK0JnNnFYK2lmY0VBYzl6MGdGaXprREI3QTQzVHVqZ09PSktvakhFSzVzSnNWR240NFJEa1NGWFNoTnNKNk8xb3NGWE01N0FxNU5nRG9VQWlzek5uSSsvSkZRckFoRG96ZU9rVWFWaStRcHJGaG5qRTQyWW9lU3k4SDVzd3E2RVlockR3Y3RuWWhZSk1rUmwyNEd2TWl6NnFER0RqT1Rod1Jpb0lING02S2NYODd4K2p1TmJZdS9ZdlJSUGY1UU9xQVZaZ1JnU09vSXloelJuVmphQW1BWldSamRDSUQvV0ZYaG9ZU1ZYNDVXUVVHK3BPakdGeTZHQ2ovZVpkUlpoYTRzMmhFNzlrbmhXUHZRSmpVVkV3cnB4bTd6akdSZU0wZUc2RDlQeXpxQWhhV3NvSGtLMjRxWmJsYXNLTG16Q2pzNGV6Z21yZmd6QjNGaXBKRUlKTkVhZ0ozSlM3WllVZ1h4ZEhpbXRvb0tEcTE5QkgyaDJhOXpsM25hNEJ4SUNHMTFIYUl5NC9RV3RpUWdmNzRvTlQ4RUVTU3JIdXFaeWxFZUhheE1PZURjUU9wUlM3aVV1SUVpMHFGa3hYdWgwTU1BVHRjMCtqNW13cUhPMFZZc1VTdHdSR2MwcFM2UXpFenFBS1hIaHQzV2wzUjNNRXlZT2tQKzRtbFp1NVFRbjdNZHVvYWsxM0E0MUR1ZE9DdTRKdmlSU0EzM0x1NEFIQit3REZmUGFxNTQ4M3c1R2VxT0Mxcy9XMU9LWVJjSTBtSS9zQUM0clNVQmUyM2Z3VVEvTDYzMS9mM1B3PT0iLCAiX0VuYWJsZWQiOiB0cnVlLCAiQnV0dG9uUGFkZGluZyI6IDAsICJNYXhUZXh0V2lkdGgiOiAwLCAiVGV4dFNpemUiOiAxMywgIkF1dG9DbG9zZU9uVXNlIjogdHJ1ZX0=" -o "ShortcutPanel.json"
```

#### Output:
<details>
<summary>Click to Expand</summary>

```shell
Output written to ShortcutPanel.json
Press Enter to close the window...
```

</details>

### UmbraXIV encoded export as file with JSON output to file
```shell
python umbraxiv_export_json_tool.py -d -f "{Input_File_Path}" -o "{Output_File_Path}"
```
#### Example:
```shell
python umbraxiv_export_json_tool.py -d -f "UmbraXIVExport.txt" -o "ShortcutPanel.json"
```

#### Output:
<details>
<summary>Click to Expand</summary>

```shell
Output written to ShortcutPanel.json
Press Enter to close the window...
```

</details>

### UmbraXIV encoded export as CLI argument with JSON output to console with Emote Name Conversion
```shell
python umbraxiv_export_json_tool.py -d -s "{UmbraXIV_Export_String}" -e
```

#### Example:
```shell
python umbraxiv_export_json_tool.py -d -c -s "WI|ShortcutPanel|eyJCdXR0b25MYWJlbCI6ICJFbW90ZSBNZW51IiwgIkJ1dHRvbkljb25JZCI6IDAsICJEZWNvcmF0ZSI6IHRydWUsICJEZXNhdHVyYXRlSWNvbiI6IGZhbHNlLCAiRGlzcGxheU1vZGUiOiAiVGV4dEFuZEljb24iLCAiSWNvbkxvY2F0aW9uIjogIkxlZnQiLCAiSWNvbkNvbG9yIjogNDI5NDk2NzI5NSwgIlRleHRBbGlnbiI6ICJMZWZ0IiwgIkljb25TaXplIjogMCwgIkljb25ZT2Zmc2V0IjogMCwgIkxhYmVsTWF4V2lkdGgiOiAwLCAiVGV4dFlPZmZzZXQiOiAwLCAiQ2F0ZWdvcnlOYW1lXzAiOiAiU2hvcnRjdXQgUGFuZWwiLCAiQ2F0ZWdvcnlOYW1lXzEiOiAiIiwgIkNhdGVnb3J5TmFtZV8yIjogIiIsICJDYXRlZ29yeU5hbWVfMyI6ICIiLCAiTnVtQ29scyI6IDE2LCAiTnVtUm93cyI6IDE2LCAiU2hvd0VtcHR5U2xvdHMiOiBmYWxzZSwgIlNsb3RDb25maWciOiAiU1BEfFhWWkxqbHd4Q0x6S3FOZVJZakQ0ay8wc2M2TFIzRDE2RkJTZDJiU0ViWXJpVjYrL1h1UDE1K01yZmwrZmYzL2JldjM2ZUltbnFXR3R1bnlzcVhWM0g5TjJtakwzWSsreVZlUDVQclJ4ZjJuN1l4K0dpdXRUc2ZROHBzNnk1VXdjTUo0ckRpckFnVDM0WU1GakVISXVIREJrQmhtV0Izc0FzamhtVEsrVU4wTDRUSHZCMzh0ZkxnQzhJbXdCb0pOVFBwQjZrRm1SQVNoNjllTkVFZFhLbGdFSEt3QVZlRmh4RklTMHlRY2dyU1E1Z0tra2RRQ2hyUFVBaHJLVUVvbktaUkNVVXU3a0FVYmxFbU1hRG5vK0JnNnFYK2lmY0VBYzl6MGdGaXprREI3QTQzVHVqZ09PSktvakhFSzVzSnNWR240NFJEa1NGWFNoTnNKNk8xb3NGWE01N0FxNU5nRG9VQWlzek5uSSsvSkZRckFoRG96ZU9rVWFWaStRcHJGaG5qRTQyWW9lU3k4SDVzd3E2RVlockR3Y3RuWWhZSk1rUmwyNEd2TWl6NnFER0RqT1Rod1Jpb0lING02S2NYODd4K2p1TmJZdS9ZdlJSUGY1UU9xQVZaZ1JnU09vSXloelJuVmphQW1BWldSamRDSUQvV0ZYaG9ZU1ZYNDVXUVVHK3BPakdGeTZHQ2ovZVpkUlpoYTRzMmhFNzlrbmhXUHZRSmpVVkV3cnB4bTd6akdSZU0wZUc2RDlQeXpxQWhhV3NvSGtLMjRxWmJsYXNLTG16Q2pzNGV6Z21yZmd6QjNGaXBKRUlKTkVhZ0ozSlM3WllVZ1h4ZEhpbXRvb0tEcTE5QkgyaDJhOXpsM25hNEJ4SUNHMTFIYUl5NC9RV3RpUWdmNzRvTlQ4RUVTU3JIdXFaeWxFZUhheE1PZURjUU9wUlM3aVV1SUVpMHFGa3hYdWgwTU1BVHRjMCtqNW13cUhPMFZZc1VTdHdSR2MwcFM2UXpFenFBS1hIaHQzV2wzUjNNRXlZT2tQKzRtbFp1NVFRbjdNZHVvYWsxM0E0MUR1ZE9DdTRKdmlSU0EzM0x1NEFIQit3REZmUGFxNTQ4M3c1R2VxT0Mxcy9XMU9LWVJjSTBtSS9zQUM0clNVQmUyM2Z3VVEvTDYzMS9mM1B3PT0iLCAiX0VuYWJsZWQiOiB0cnVlLCAiQnV0dG9uUGFkZGluZyI6IDAsICJNYXhUZXh0V2lkdGgiOiAwLCAiVGV4dFNpemUiOiAxMywgIkF1dG9DbG9zZU9uVXNlIjogdHJ1ZX0="
```

#### Output:
<details>
<summary>Click to Expand</summary>

```shell
{
    "ButtonLabel": "Emote Menu",
    "ButtonIconId": 0,
    "Decorate": true,
    "DesaturateIcon": false,
    "DisplayMode": "TextAndIcon",
    "IconLocation": "Left",
    "IconColor": 4294967295,
    "TextAlign": "Left",
    "IconSize": 0,
    "IconYOffset": 0,
    "LabelMaxWidth": 0,
    "TextYOffset": 0,
    "CategoryName_0": "Shortcut Panel",
    "CategoryName_1": "",
    "CategoryName_2": "",
    "CategoryName_3": "",
    "NumCols": 16,
    "NumRows": 16,
    "ShowEmptySlots": false,
    "SlotConfig": {
        "0": {
            "0": "EM/Blow Kiss",
            "1": "EM/Rally",
            "2": "EM/Laugh",
            "3": "EM/Psych",
            "4": "EM/Thumbs Up",
            "5": "EM/Hug",
            "6": "EM/Welcome",
            "8": "EM/Huh",
            "9": "EM/Stagger",
            "10": "EM/Furious",
            "11": "EM/Disappointed",
            "12": "EM/Clutch Head",
            "13": "EM/Clutch Head",
            "14": "EM/Aback",
            "15": "EM/Angry",
            "16": "EM/Blush",
            "17": "EM/Battle Stance",
            "18": "EM/Wow",
            "19": "EM/Joy",
            "20": "EM/Victory",
            "21": "EM/Pray",
            "22": "EM/Cheer",
            "24": "EM/Headache",
            "25": "EM/Upset",
            "26": "EM/Slap",
            "27": "EM/Panic",
            "28": "EM/Angry",
            "29": "EM/No",
            "30": "EM/Cry",
            "31": "EM/Deny",
            "32": "EM/Congratulate",
            "33": "EM/Clap",
            "34": "EM/Happy",
            "35": "EM/Hug",
            "36": "EM/Victory Reveal",
            "37": "EM/Most Gentlemanly",
            "38": "EM/Dote",
            "41": "EM/Sulk",
            "42": "EM/Shrug",
            "43": "EM/Shocked",
            "44": "EM/Fume",
            "45": "EM/No",
            "46": "EM/Grovel",
            "47": "EM/Facepalm",
            "48": "EM/Comfort",
            "49": "EM/Chuckle",
            "50": "EM/Eureka",
            "51": "EM/Snap",
            "52": "EM/Yes",
            "53": "EM/Surprised",
            "54": "EM/Fist Pump",
            "76": "EM/Paint It Yellow",
            "77": "EM/Paint It Black",
            "78": "EM/Paint It Blue",
            "79": "EM/Paint It Red",
            "80": "EM/Lookout",
            "81": "EM/Converse",
            "82": "EM/Box",
            "83": "EM/Frighten",
            "84": "EM/Stretch",
            "85": "EM/Point",
            "86": "EM/Poke",
            "87": "EM/Tomestone",
            "88": "EM/Pay Respects",
            "89": "EM/Hand Over",
            "92": "EM/Uchiwasshoi",
            "93": "EM/Toast",
            "94": "EM/Break Fast",
            "95": "EM/Eat Apple",
            "96": "EM/Flex",
            "97": "EM/Shush",
            "98": "EM/Air Quotes",
            "99": "EM/Me",
            "100": "EM/Pose",
            "101": "EM/Soothe",
            "102": "EM/Examine Self",
            "103": "EM/Squats",
            "104": "EM/Think",
            "105": "EM/High Five",
            "128": "EM/Goodbye",
            "129": "EM/Greeting",
            "130": "EM/Wave",
            "140": "EM/Scared",
            "141": "EM/Confused",
            "142": "EM/Ouch",
            "143": "EM/Sad",
            "144": "EM/Bow",
            "145": "EM/Eastern Bow",
            "146": "EM/Imperial Salute",
            "147": "EM/Storm Salute",
            "148": "EM/Salute",
            "157": "EM/Annoyed",
            "158": "EM/Sneer",
            "159": "EM/Worried",
            "176": "EM/Doze",
            "177": "EM/Kneel",
            "178": "EM/Sit",
            "179": "EM/Show Right",
            "180": "EM/Show Left",
            "181": "EM/Malevolence",
            "182": "EM/Lean",
            "183": "EM/Guard",
            "184": "EM/Read",
            "188": "EM/Wink (Right)",
            "189": "EM/Wink (Left)",
            "190": "EM/Smile",
            "191": "EM/Simper",
            "192": "EM/Yellow Ranger Pose B",
            "193": "EM/Yellow Ranger Pose A",
            "194": "EM/Black Ranger Pose A",
            "195": "EM/Black Ranger Pose B",
            "196": "EM/Red Ranger Pose B",
            "197": "EM/Red Ranger Pose A",
            "198": "EM/Sit on Ground",
            "199": "EM/At Ease",
            "200": "EM/Attention",
            "201": "EM/Play Dead",
            "204": "EM/Grin",
            "205": "EM/Fake Smile",
            "206": "EM/Content",
            "207": "EM/Beam",
            "208": "EM/Push-ups",
            "209": "EM/Charmed",
            "210": "EM/Breath Control",
            "211": "EM/Cheer On",
            "212": "EM/Cheer Jump",
            "213": "EM/Hum",
            "214": "EM/Sit-ups",
            "215": "EM/Sweep Up",
            "216": "EM/Wring Hands",
            "217": "EM/Water Float",
            "224": "EM/Manderville Dance",
            "225": "EM/Popoto Step",
            "226": "EM/Step Dance",
            "227": "EM/Thavnairian Dance",
            "234": "EM/Amazed",
            "235": "EM/Concentrate",
            "236": "EM/Ponder",
            "237": "EM/Pucker Up",
            "238": "EM/Reflect",
            "239": "EM/Furrow",
            "240": "EM/Ball Dance",
            "241": "EM/Bee's Knees",
            "242": "EM/Dance",
            "243": "EM/Flame Dance",
            "249": "EM/Alert",
            "250": "EM/Scoff",
            "251": "EM/Shut Eyes",
            "252": "EM/Taunt",
            "253": "EM/Straight Face",
            "254": "EM/Endure",
            "255": "EM/Smirk"
        }
    },
    "_Enabled": true,
    "ButtonPadding": 0,
    "MaxTextWidth": 0,
    "TextSize": 13,
    "AutoCloseOnUse": true
}
Press Enter to close the window...
```

</details>