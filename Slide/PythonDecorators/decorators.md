# Decorators

<img src="http://dellatorrespa.com/wp-content/uploads/2016/10/fake-christmas-trees-are-toxic-alternatives.jpg" style="width:400px">

--

http://book42qu.readthedocs.io/en/latest/python/python-closures-and-decorators.html

--

## Closure 閉包

* OOP Encapsulation
* 不需用到 class、又可以讓函數可以存取得到某些專屬的變數

--

## 情境一: Debugging

* 想要在函數進入點印出訊息。

```python
class MyClass:

  def construct_hi(self):
    # print("This is debug message")
    return "hi"

  def construct_hello(self):
    # print("This is debug message")
    return "hello"

if __name__ == "__main__":
  obj = MyClass()
  print(obj.construct_hi())
  print(obj.construct_hello())
```

--

```py
class DebugMyClass(MyClass):
    def construct_hi(self):
        print("This is debug message")
        return super(DebugMyClass, self).construct_hi()

    def construct_hello(self):
        print("This is debug message")
        return super(DebugMyClass, self).construct_hello()
```

--

## Function Wrapper

```py
def debug_wrapper(f):
    def wrap_f(*args, **kargs):
        print("This is debug message")
        return f(*args, **kargs)
    return wrap_f
```

--

## Class Wrapper

```py
class DebugWrapper(object):
    def __init__(self, wrapped_class):
        self.wrapped_class = wrapped_class()

    def __getattr__(self, attr):
        orig_attr = self.wrapped_class.__getattribute__(attr)
        if callable(orig_attr):
            def wrap_f(*args, **kwargs):
                # Begin of function call
                print("This is debug message")
                result = orig_attr(*args, **kwargs)
                # prevent wrapped_class from becoming unwrapped
                ### if result == self.wrapped_class:
                ###    return self
                # End of function call
                return result
            return wrap_f
        else:
            return orig_attr
```

--

## Decorator 修飾器

http://ot-note.logdown.com/posts/67571/-decorator-with-without-arguments-in-function-class-form


--

```py
def debug_wrapper(f):
    # 這裡的空間就是 closure!
    def wrap_f(*args, **kargs):
        print("This is debug message")
        return f(*args, **kargs)
    return wrap_f
```


```py
class MyClass:

  @debug_wrapper
  def construct_hi(self):
    return "hi"

  @debug_wrapper
  def construct_hello(self):
    return "hello"
```

--

## Closure 的功用

* 想知道這個函式被呼叫了幾次？

--

```py
def debug_wrapper(f):
    counter = 0
    def wrap_f(*args, **kargs):
        nonlocal counter
        counter += 1
        print("This is debug message (%d)" % counter)
        return f(*args, **kargs)
    return wrap_f
```
