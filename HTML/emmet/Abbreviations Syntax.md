# Emmet
[관련 사이트](http://docs.emmet.io/abbreviations/syntax/)
## Abbreviations Syntax
### Elements
미리 정의된 태그 이름들이 없으므로, 단어를 쓰고 태그로 변환이 가능합니다.  
ex) foo -> \<foo>\</foo>  
### Nesting operators
중첩 연산자는 트리 내부에 약어 요소를 배치하는데 사용됩니다.  
#### Child: >
`div>ul>li`

```html
<div>
	<ul>
		<li></li>
	</ul>
</div>
```

#### Sibling: +
`div+p+bq`

```html
<div></div>
<p></p>
<blockquote></blockquote>
```

#### Climb-up: ^
`div+div>p>span+em`

```html
<div></div>
<div>
	<p><span></span><em></em></p>
</div>
```

`div+div>p>span>em^bq`

```html
<div></div>
<div>
	<p><span></span><em></em></p>
	<blockquote></blockquote>
</div>
```
여러개 사용 가능합니다.  
`div+div>p>span+em^^^bq`

```html
<div></div>
<div>
	<p><span></span><em></em></p>
</div>
<blockquote></blockquote>
```

#### Multiplication: *
`ul>li*5`

```html
<ul>
	<li></li>
	<li></li>
	<li></li>
	<li></li>
	<li></li>
</ul>
```

#### Grouping: ()
`div>(header>ul>li*2>a)+footer>p`

```html
<div>
	<header>
		<ul>
			<li><a href=""></a></li>
			<li><a href=""></a></li>
		</ul>
	</header>
	<footer>
		<p></p>
	</footer>
</div>
```
그룹을 중첩하여 곱셈 연산자와 결합이 가능합니다.  
`(div>dl>(dt+dd)*3)+footer>p`

```html
<div>
	<dl>
		<dt></dt>
		<dd></dd>
		<dt></dt>
		<dd></dd>
		<dt></dt>
		<dd></dd>
	</dl>
</div>
<footer>
	<p></p>
</footer>
```

### Attribute operators

#### ID and CLASS
`div#header+div.page+div#footer.class1.class2.class3`

```html
<div id="header"></div>
<div class="page"></div>
<div id="footer" class="class1 class2 class3"></div>
```

#### Custom attributes
`td[title="Hello world!" colspan=3]`

```html
<td title="Hello world!" colspan="3"></td>
```

#### Item numbering: $
`ul>li.item$*5`

```html
<ul>
	<li class="item1"></li>
	<li class="item2"></li>
	<li class="item3"></li>
	<li class="item4"></li>
	<li class="item5"></li>
</ul>
```

`ul>li.item$$$*5`

```html
<ul>
	<li class="item001"></li>
	<li class="item002"></li>
	<li class="item003"></li>
	<li class="item004"></li>
	<li class="item005"></li>
</ul>	
```

#### Changing numbering base and direction
`ul>li.item$@-*5`

```html
<ul>
	<li class="item5"></li>
	<li class="item4"></li>
	<li class="item3"></li>
	<li class="item2"></li>
	<li class="item1"></li>
</ul>
```

`ul>li.item$@3*5`

```html
<ul>
	<li class="item3"></li>
	<li class="item4"></li>
	<li class="item5"></li>
	<li class="item6"></li>
	<li class="item7"></li>
</ul>
```

`ul>li.item$@-3*5`

```html
<ul>
	<li class="item7"></li>
	<li class="item6"></li>
	<li class="item5"></li>
	<li class="item4"></li>
	<li class="item3"></li>
</ul>
```

### Text: {}
`a{Click me}`

```html
<a href="">Click me</a>
```

\> 연산자를 명시적으로 사용할 경우 트리 구조로 됩니다.  
`a{click}+b{here}`

```html
<!-- a{click}+b{here} -->
<a href="">click</a><b>here</b>
```

`a>{click}+b{here}`

```html
<!-- a>{click}+b{here} -->
<a href="">click<b>here</b></a>
```

`p>{Click }+a{here}+{ to Continue}`

```html
<p>Click <a href="">here</a> to continue</p>
```

`p{Click }+a{here}+{ to continue}`

```html
<p>Click </p>
<a href="">here</a> to continue
```

### Notes on abbreviation formatting
약어에 익숙해져서 구문을 편히 볼 수 있게 space를 넣으면 작동하지 않는다.  
space는 Emmet의 약어 구분 기능을 멈추라는 신호이기 때문이다.