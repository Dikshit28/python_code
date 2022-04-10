from mrjob.job import MRJob

class WordCount(MRJob):
    def mapper(self, _, line):
        for sen in line.split("\n"):
            for i in range(len(sen)):
                words=sen[i].split(" ")
                for word in words:
                    yield word.lower(), 1

    def reducer(self, word, counts):
        yield word.lower(), sum(counts)

if __name__ == '__main__':
    WordCount.run()