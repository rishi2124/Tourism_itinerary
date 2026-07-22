"""
Document Generator

Converts the master tourism dataset into rich knowledge documents
for ChromaDB ingestion.
"""

import pandas as pd


class DocumentGenerator:
    """
    Generates rich documents from the master tourism dataset.
    """

    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path)

    def generate_documents(self):
        """
        Reads the dataset and returns a list of documents.
        """
        pass


if __name__ == "__main__":

    generator = DocumentGenerator(
        "data/processed/master_varanasi_attractions.csv"
    )

    print(generator.df.head())

    print(f"\nLoaded {len(generator.df)} attractions successfully.")