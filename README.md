# japanization-tools

## Usage

```bash
git clone https://github.com/mikoim/japanization-tools.git
cd japanization-tools
pip3.5 install -r requirements.txt

# Generate BB Code files based on "日本語化情報DB".
# These files will be outputted at "output" directory.
python3.5 generate_files.py

# Gather recommended games on Steam Group
python3.5 gather_curation.py | tee result.txt

# Gather game information on Steam Store by appid
python3.5 appid.py 730
```
