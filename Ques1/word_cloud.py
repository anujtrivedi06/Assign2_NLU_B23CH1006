import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_word_cloud(file_path):
    # 1. Load the cleaned corpus
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 2. Configure the WordCloud
    # We exclude common 'stopwords' (the, is, at) to show meaningful academic terms
    wordcloud = WordCloud(
        width=800, 
        height=400,
        background_color='white',
        colormap='viridis',
        max_words=150
    ).generate(text)

    # 3. Display and Save
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Most Frequent Words in IIT Jodhpur Corpus")
    plt.savefig('wordcloud_iitj.png')
    plt.show()

if __name__ == "__main__":
    generate_word_cloud('corpus.txt')