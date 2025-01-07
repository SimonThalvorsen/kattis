#!/bin/bash

# Constants
SRC_FOLDER="src"
README_FILE="README.md"
LANGUAGE_FOLDER_MAP=("python:Python 3" "c:C" "cpp:C++" "java:Java")
EXTENSION_MAP=("python:.py" "c:.c" "cpp:.cpp" "java:.java")
REPO_URL="https://github.com/SimonThalvorsen/kattis/tree/master"

# Helper functions
get_language_folder() {
    for pair in "${LANGUAGE_FOLDER_MAP[@]}"; do
        if [[ $pair == "$1:"* ]]; then
            echo "${pair#*:}"
            return
        fi
    done
    echo "Unsupported language" && exit 1
}

get_file_extension() {
    for pair in "${EXTENSION_MAP[@]}"; do
        if [[ $pair == "$1:"* ]]; then
            echo "${pair#*:}"
            return
        fi
    done
    echo "Unsupported language" && exit 1
}

extract_problem_name() {
    local url=$1
    echo "${url##*/}"
}

generate_readme_entry() {
    local problem_name=$1
    local problem_url=$2
    local language=$3
    local lang_folder=$(get_language_folder "$language")
    local rel_path="$REPO_URL/$SRC_FOLDER/$problem_name/$lang_folder"
    local kattis_link="[![:cat:](https://open.kattis.com/favicon)]($problem_url)"
    echo "| [$problem_name]($rel_path) | [$lang_folder]($rel_path) | $kattis_link |"
}

update_readme() {
    local entry=$1

    # Create README if it doesn't exist
    if [[ ! -f $README_FILE ]]; then
        echo "## Problems" > "$README_FILE"
        echo "| Problem | Languages | :link: |" >> "$README_FILE"
        echo "| - | - | - |" >> "$README_FILE"
    fi

    # Add the new entry
    if ! grep -qF "$entry" "$README_FILE"; then
        echo "$entry" >> "$README_FILE"
    fi

    # Sort entries alphabetically, excluding the header
    local header=$(head -n 3 "$README_FILE")
    local body=$(tail -n +4 "$README_FILE" | sort -f)
    echo -e "$header\n$body" > "$README_FILE"
}

create_problem_structure() {
    local problem_name=$1
    local language=$2
    local lang_folder=$(get_language_folder "$language")
    local problem_path="$SRC_FOLDER/$problem_name/$lang_folder"
    mkdir -p "$problem_path"
    echo "$problem_path"
}

# Main logic
if [[ $# -lt 2 ]]; then
    echo "Usage: ./kattis_script.sh URL_TO_PROBLEM <programming_language>"
    exit 1
fi

problem_url=$1
language=$2
editor=${EDITOR:-vim}

problem_name=$(extract_problem_name "$problem_url")
file_extension=$(get_file_extension "$language")
file_name="$problem_name$file_extension"
problem_path=$(create_problem_structure "$problem_name" "$language")
file_path="$problem_path/$file_name"

# Create the file if it doesn't exist
if [[ ! -f $file_path ]]; then
    echo "// Solution for $problem_name in $(get_language_folder "$language")" > "$file_path"
fi

# Generate and update the README entry
readme_entry=$(generate_readme_entry "$problem_name" "$problem_url" "$language")
update_readme "$readme_entry"

# Add the file to Git and open in editor
git add "$file_path"
git add "$README_FILE"
$editor "$file_path"

echo "File $file_path created, README updated, and file added to git."
