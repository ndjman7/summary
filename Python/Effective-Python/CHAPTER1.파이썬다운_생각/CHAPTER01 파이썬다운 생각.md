# CHAPTER01 파이썬다운 생각
프로그래밍 언어에서 사용하는 용어는 그 언어을 쓰는 사용자들에 의해 정의된다.  
수년 동안 파이썬 커뮤니티는 특정 스타일을 따르는 코드를 '파이썬다운'이라는 형용사로 표현해왔다.  
파이썬 프로그래머들은 복잡함 보다는 단순함을, 가독성을 위해 명료한 것을 좋아한다.

파이선 쉘에서 `import this`를 입력할 경우,

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

파이썬을 '파이썬답게'하는 것이 가장 중요하다.

## BETTER WAY 1 사용 중인 파이썬의 버전을 알자
책은 3.4 문법에 기반을 둔다.

파이썬의 명령어를 알려면 다음과 같이 --version을 사용하면 된다.

`$ python --version`

파이썬3는 다음과 같다.

`$ python3 --verison`

파이썬에 내장된 sys 모듈 안의 값을 조사하여 런타임에 사용 중인 파이썬의 버전을 알아낼 수도 있다.

```python
import sys
print(sys.version_info)
print(sys.version)
```

```
>>>
sys.version_info(major=3, minor=4, micro=2, releaselevel='final', serial=0)
3.4.2 (default, Jan  5 2017, 12:52:39)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)]
```

파이썬2를 2to3, six같은 도구를 사용하면 파이썬 3로 더 쉽게 옮겨갈 수 있다.

__핵심정리__
> - 파이썬3를 쓰자. (파이썬2는 2020년에 지원 중단 [링크](https://pythonclock.org/))
> - 파이썬에는 CPython,Jython,IronPython,PyPy 같은 다양한 런타임이 있다.
> - 시스템에서 파이썬을 실행하는 명령이 사용하고자 하는 파이썬 버전인지 확인해야 한다.