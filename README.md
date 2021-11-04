# clean-epub

The excellent [knock](https://github.com/BentonEdmondson/knock) application by Benton Edmondson outputs EPUBs that seem to be DRM-free. However, if you run the application twice on the same ACSM file, the hashes do not match.

This script normalizes EPUB files, and it is specifically written to normalize the output files of knock. It strips away all the differences between different EPUB files for the same book.

## Usage

`./clean-epub.py -i input.epub -o output.epub`

## Details

In essence, it does this:
- Create a temporary directory, and unzip the input EPUB into it
- Set all the access and modification times for files and directories in the temporary directory to a fixed date
- Zip the contents of the temporary directory into a new EPUB, without adding extra file attributes

I tested it on Ubuntu 20.04, with EPUBs bought from Bol(dot)com.

There are three reasons why you might want to test it more extensively before depending on it:
- Ebooks from other sellers might contain more identifying details than just the zip order and timestamps.
- The zip implementation of another OS might not deterministically order the input files of the new zip file.
- Your OS might track more file metadata fields than just access and modification times (not sure if this exists)
