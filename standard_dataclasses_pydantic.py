from pydantic import BaseModel
from dataclasses import dataclass
from typing import List, Dict, Tuple


#when we want to define and describe a function
def andrey(request: Dict) -> Tuple[List[int], Dict]:
    pass

class Student1:
    def __init__(self, uid, name, age, subjects):
        try:
            uid = int(uid)
            name = str(name)
            age = int(age)
            self.uid = uid
            self.name = name
            self.age = age
            if isinstance(subjects, List):
                for el in subjects:
                    if isinstance(el, str):
                        continue
                else:
                    self.subjects = subjects

        except Exception as e:
            print(e)

    def __str__(self):
        return f'{self.uid}({type(self.uid)})    {self.name}({type(self.name)})'


class Student2(BaseModel):
    uid: int
    name: str
    age: int
    subjects: List[str]

    def __str__(self):
        return f'{self.uid}({type(self.uid)})    {self.name}({type(self.name)})'

@dataclass
class Student3:
    uid: int
    name: str
    age: int
    subjects: List[str]

    def __str__(self):
        return f'{self.uid}({type(self.uid)})    {self.name}({type(self.name)})'


if __name__ == '__main__':
    s1 = Student1('43', 'Ivo', 35)
    print(s1)

    s2 = Student2(uid='2134', name='Ivo', age=35)
    print(s2)

    s3 = Student2(uid='44444', name='Ivo', age=35)
    print(s3)
