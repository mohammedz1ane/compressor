# Project Compressor

Project Compressor is a powerful, cross-platform command-line tool designed to help developers and web designers optimize their digital assets. By efficiently compressing images and PDFs, it enables faster website loading times, improved user experience, and reduced bandwidth usage.

## Why Use Project Compressor?

As a programmer or web developer, you often need to manage numerous images and documents for your websites or applications. Large file sizes can significantly impact your site's performance, affecting user experience and SEO rankings. Project Compressor addresses this challenge by:

- Reducing image file sizes without noticeable quality loss
- Compressing PDFs to minimize document sizes
- Batch processing multiple files, saving you time and effort
- Providing a simple command-line interface for easy integration into your workflow or build processes

By using Project Compressor before uploading assets to your website, you can:

- Improve page load times
- Reduce bandwidth usage and associated costs
- Enhance overall site performance
- Potentially improve SEO rankings (as site speed is a ranking factor)

## Features

- Compress image files (JPG, JPEG, PNG, GIF) with optimized settings for web use
- Compress PDF files to reduce size while maintaining readability (placeholder)
- Convert DOCX and PPTX files to compressed PDFs (placeholder)
- Batch compression of all supported files in a directory
- Compress or extract ZIP archives
- Cross-platform support (Windows and Unix-like systems)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/mohammedz1ane/compressor.git
   cd compressor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the command for global use:

   For Windows:
   - Edit the system PATH environment variable and add the directory containing the `compress.bat` file.
        ```batch
        @echo off
        python "%~dp0compress.py" %*
        ```

This batch file does the following:

1. `@echo off` prevents the commands from being printed in the console.
2. `%~dp0`

   For Unix-like systems:
   - Make the `compress` script executable:
     ```
     chmod +x compress
     ```
   - Move the script to a directory in your PATH:
     ```
     sudo mv compress /usr/local/bin/
     ```

## Usage

After installation, you can use the `compress` command from any directory in your project:

```
compress [OPTIONS]
```

### Options:

- `-a`: Compress all PDF and image files in the current directory
- `-f FILE_NAME`: Compress the specified PDF or image file
- `-c FILE_NAME`: Convert the specified DOCX or PPTX file to PDF (placeholder)
- `-e [NAME]`: Compress or extract the specified file/folder, or compress the current directory if no argument is provided
- `-h, --help`: Show the help message and exit

### Examples:

```
compress -a                  # Compress all supported files in the current directory
compress -f logo.png         # Compress a specific image file
compress -e assets           # Compress the 'assets' folder into a ZIP archive
compress -c document.docx    # Convert and compress a DOCX file to PDF (placeholder)
```

## Workflow Integration

Project Compressor can be easily integrated into your development workflow:

1. **Pre-commit Hook**: Set up a pre-commit hook to automatically compress new or modified images before committing them to your repository.

2. **Build Process**: Incorporate Project Compressor into your build process to optimize assets before deployment.

3. **Batch Processing**: Use the `-a` option to quickly optimize all assets in a project directory before pushing updates to your website.

## Limitations

- PDF compression and document conversion (DOCX/PPTX to PDF) are currently placeholder functions and not fully implemented.
- RAR extraction is not implemented in this version.

## Requirements

- Python 3.6+
- Pillow library for image processing

## Contributing

Contributions to improve Project Compressor are welcome. Whether it's adding new features, improving compression algorithms, or enhancing cross-platform compatibility, your input is valuable. Please feel free to submit a Pull Request.

