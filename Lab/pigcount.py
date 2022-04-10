from mrjob.job import MRJob

class WordCount(MRJob):
    def mapper(self, _, file):
        lines=file.split('\n')
        for line in lines:
            for words in line.split(' '):
                word=words.strip()
                if word=="" or word==" " or len(word)<2:
                    continue
                yield ''.join(char for char in word if char.isalnum()).lower(),1

    def reducer(self, word, counts):
        yield word.lower(), sum(counts)

if __name__ == '__main__':
    WordCount.run()