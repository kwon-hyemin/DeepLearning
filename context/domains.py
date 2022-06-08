# dname, fname, train, test, id, label
from dataclasses import dataclass
from abc import *
import pandas
import pandas as pd
import googlemaps


@dataclass
class File(object):
    context: str
    fname: str
    dframe: object

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> str: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe


@dataclass()
class Dataset:
    dname: str
    sname: str
    fname: str
    train: pandas.core.frame.DataFrame
    test: pandas.core.frame.DataFrame
    id: str
    label: str

    @property
    def dname(self) -> str: return self._dname

    @dname.setter
    def dname(self, value): self._dname = value

    @property
    def sname(self) -> str: return self._sname

    @sname.setter
    def sname(self, sname): self._sname = sname

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, value): self._fname = value

    @property
    def train(self) -> pandas.core.frame.DataFrame: return self._train

    @train.setter
    def train(self, value): self._train = value

    @property
    def test(self) -> pandas.core.frame.DataFrame: return self._test

    @test.setter
    def test(self, value): self._test = value

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, value): self._id = value

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, value): self._label = value


class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass

    # new_file, csv, xls, json


class ReaderBase(metaclass=ABCMeta):
    @abstractmethod
    def new_file(self, file) -> str:
        pass

    @abstractmethod
    def csv(self, fname) -> object:
        pass

    @abstractmethod
    def xls(self, fname) -> object:
        pass

    @abstractmethod
    def json(self, fname) -> object:
        pass


# Reader가 ReaderBase 의 자식이다
class Reader(ReaderBase):
    def new_file(self, file) -> str:
        # 파일하고 파일경로하고 분리시켜둬야한다
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}', encoding='UTF-8', thousands=',')

    def xls(self, file, header, cols) -> object:
        return pd.read_excel(f'{self.new_file(file)}', header=header, usecols=cols)

    def json(self, file) -> object:
        return pd.read_json(f'{self.new_file(file)}', encoding='UTF-8')

    def gmaps(self) -> object:
        return googlemaps.Client(key='')

    def myprint(self, this):
        print('*' * 100)
        print(f'1. Target type \n {type(this)} ')
        print(f'2. Target column \n {this.columns} ')
        print(f'3. Target top 1개 행\n {this.head(1)} ')
        print(f'4. Target bottom 1개 행\n {this.tail(1)} ')
        print(f'4. Target null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)
