from modules.module1 import get_source as get_source1
from modules.module2 import get_source as get_source2
from my_package.folder1.file1 import get_source as get_source3
from my_package.folder1.file2 import get_source as get_source4
from my_package.folder2.file1 import get_source as get_source5
from my_package.folder3.file1 import get_source as get_source6
from my_package.folder3.folder4.file1 import get_source as get_source7

if __name__ == "__main__":
    print(get_source1())
    print(get_source2())
    print(get_source3())
    print(get_source4())
    print(get_source5())
    print(get_source6())
    print(get_source7())
