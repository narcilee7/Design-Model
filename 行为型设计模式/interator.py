# 迭代器模式

from collections.abc import Iterator, Iterable

# 自定义聚合类
class WordsCollection(Iterable):
  def __init__(self, words: list[str]):
    self.words = words

  def add_word(self, word: str):
    self.words.append(word)

  def __iter__(self) -> Iterator:
    return WordsIterator(self.words)

# 自定义迭代器
class WordsIterator(Iterator):
  def __init__(self, words: list[str]):
    self._index = 0
    self._words = words

  def __next__(self):
    if self._index < len(self._words):
      result = self._words[self._index]
      self._index += 1
      return result
    raise StopIteration

# 使用
words_collection = WordsCollection(["Hello", "World", "Python"])
words_collection.add_word("Java")

for word in words_collection:
  print(word)