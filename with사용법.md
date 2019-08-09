# with사용법
with는 파일처리에 관한 것 </br>

> 1. 파일열고</br>
2. 파일처리</br>
3. 파일닫고</br>

파일을 열었으면 닫는 작업을 항상 해야 한다. </br>
with as 는 자동으로 마무리 해줌 ~~ </br>
내부적으로 **__exit__()**, **__enter__()**가 구현이 되있다. </br>

```python
with open('output.txt', 'w') as f:
	f.write('Hi there!')

with open('test.data') as data_file: 
  print(data_file.readline(),end = "")
```
