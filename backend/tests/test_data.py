"""
Test dataset for RAGAS evaluation of the Stirling University RAG chatbot.
Ground truth answers sourced directly from Stirling University website.
"""
from datasets import Dataset

# Comprehensive test cases with real ground truth from Stirling University website
test_qa_pairs = {
    "question": [
        "How much does an undergraduate course cost for international students at Stirling University?",
        "What accommodation is available on the Stirling University campus?",
        "Where is Stirling University campus located?",
        "How many students study at Stirling University?",
        "What facilities are available in student accommodation?",
        "What is included in Stirling University accommodation rent?",
        "How many rooms does Stirling University accommodation have?",
        "What are the different types of accommodation available?",
        "Are there catering facilities on campus?",
        "How many nationalities are represented at Stirling University?",
    ],
    "ground_truth": [
        "International undergraduate tuition fees at Stirling University range from GBP 17,200 to GBP 23,700 per year, with specific fees varying by course. The university also offers scholarships ranging from GBP 2,000 to 4,000 per year to eligible students.",
        "Stirling University offers accommodation with over 2,800 rooms available right on the beautiful 330-acre campus, as well as easy-to-reach off-campus residences.",
        "Stirling University campus is set within 330 acres of grounds beneath the Ochil Hills, located 2 miles from the centre of Stirling in Scotland, close to the town of Bridge of Allan.",
        "The University of Stirling has 17,500+ students from 140+ nationalities studying globally. This includes 6,000 students in their growing postgraduate community. More than 30% of students come from an international background.",
        "University accommodation includes laundrettes. Although all accommodation is self-catered, on campus there is Refresh Bistro for breakfast, lunch or dinner, as well as other catering outlets across campus. All kitchens have a cooker, fridge, freezer, microwave and kettle.",
        "Utilities, Wi-Fi, room and contents insurance, bedding and bed linen, housekeeping assistance and 24/7 staff assistance are all included in the rent for University of Stirling accommodation.",
        "Stirling University accommodation has over 2,800 rooms available right on the campus.",
        "Stirling University offers different accommodation types: Shared Rooms are the most affordable with weekly rents ranging from £80 to £120, usually involving sharing a kitchen and bathroom. En-suite Rooms offer a private bathroom with shared kitchen facilities, costing between £120 and £180 per week.",
        "Yes, on campus there is Refresh Bistro for breakfast, lunch or dinner, as well as more than a dozen other restaurants and cafes across campus.",
        "Stirling University represents over 140 nationalities among its student population, with more than 30% of students coming from an international background.",
    ]
}

def get_test_dataset():
    """Return the test dataset as a Hugging Face Dataset object."""
    return Dataset.from_dict(test_qa_pairs)

if __name__ == "__main__":
    dataset = get_test_dataset()
    print(f"Loaded test dataset with {len(dataset)} QA pairs")
    print("\nSample questions:")
    for i, q in enumerate(dataset["question"][:3], 1):
        print(f"{i}. {q}")
