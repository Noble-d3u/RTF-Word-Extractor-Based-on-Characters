import re
import csv


class Words:
    def __init__(self, group: str):
        """Initialize the Words object with an initial group."""
        self.word_bank: dict[str, dict] = {}
        self.groups = [group]
        self.current_group_index = 0

    def add_word(self, word: str) -> None:
        """Add a word to the word bank and increment its count in the current group."""
        d = self.word_bank.get(word, {})
        d[self.current_group_index] = self.word_bank.get(word).get(self.current_group_index) + 1 if self.word_bank.get(word, {}).get(self.current_group_index, None) is not None else 1
        self.word_bank[word] = d

    def set_new_group(self, group: str):
        """Add a new group and set it as the current group."""
        self.groups.append(group)
        self.current_group_index = self.groups.index(group)


def process_rtf(path: str, char_list: list[str], word_bank: Words):
    """
    Process an RTF file to extract words containing specific characters.

    Args:
        path: Path to the RTF file.
        char_list: List of special characters to look for.
        word_bank: Words object to store the processed words.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        # Decode unicode escape sequences
        content = re.sub(r'\\u(-?\d+)?\??', lambda m: chr(int(m.group(1))), content)

        # Remove RTF control words and extract text
        sanitized = re.sub(r'\\[^ ]+|\{.*?}|\}', '', content)
        word_list = re.findall(r'\b\w+\b', sanitized)

        for word in word_list:
            if any(c in word for c in char_list):
                word_bank.add_word(word.lower())

    except FileNotFoundError:
        print(f"Error: {path} does not exist.")
    except Exception as e:
        print(f"Error processing file {path}: {e}")


def make_csv(word_bank: Words, char_list: list[str], output_path: str):
    """
    Create a CSV file summarizing word occurrences.

    Args:
        word_bank: Words object containing word counts.
        char_list: List of special characters to include.
        output_path: Path to the output CSV file.
    """
    with open(output_path, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=';')

        # Write header row
        header = ['Word', 'Character'] + word_bank.groups
        writer.writerow(header)

        # Write word data
        for word, counts in word_bank.word_bank.items():
            row = [word, next((c for c in word if c in char_list), "")]
            for group_index in range(len(word_bank.groups)):
                row.append(str(counts.get(group_index, "")))
            writer.writerow(row)


def main():
    char_list = ["à", "è", "é", "ì", "ò", "ù"]
    word_bank = Words("First File")

    # Process first RTF file
    process_rtf(path="file1.rtf", char_list=char_list, word_bank=word_bank)

    # Process second RTF file
    word_bank.set_new_group("Second File")
    process_rtf(path="file2.rtf", char_list=char_list, word_bank=word_bank)

    # Generate CSV output
    make_csv(word_bank=word_bank, char_list=char_list, output_path="word_bank.csv")


if __name__ == "__main__":
    main()
