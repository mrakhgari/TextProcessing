from Category import Category
import sys

TOKEN = '@@@@@@@@@@'
categories = []


def add_to_categories(line):
    category_name = line[0]
    category_sentence = line[1]

    if category_name not in categories:
        categories.append(Category(category_name))

    categories[categories.index(category_name)].add_sentence(category_sentence)


def save_file(file_name, words_list):
    f = open(file_name, 'w')
    for word in words_list:
        f.write(str(word[0]) +  ' ' + str(word[1]) + '\n')
    f.close()

def save_ngrams_to_file():
    for category in categories:
        save_file('./Ngrams/' + category.get_name() + '-1.txt', category.get_unigrams().items())
        save_file('./Ngrams/' + category.get_name() + '-2.txt', category.get_bigrams().items())



def main(file_path="./dataset/HAM-Train.txt"):
    try:
        f = open(file_path, 'r')
        print('file opened...')
    except OSError as e:
        print('error in opening training file, error message is: ' + e.strerror)
        sys.exit()
    i=0
    for line in f:
        i+=1
        print(i)
        add_to_categories(line.split((TOKEN)))

    save_ngrams_to_file()


if __name__ == "__main__":
    main()

    print('end')
