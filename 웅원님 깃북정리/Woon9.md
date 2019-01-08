출처 : https://dnddnjs.gitbooks.io/rl/content/value_function_approximation.html
/*이웅원님 Git*/

# Value function Approximation

## 1. Tabular Methods

  지금까지 살펴본 강화학습은 action value funciton을 Table로 만들어서 푸는 Tabular Methods입니다. 이에 대해서 Sutton교수님은 책에서 다음과 같이 이야기합니다. 즉, 현재의 방법은 state나 action이 작을 경우에만 적용 가능하다는 것입니다. 이 Table이 점점 더 커지면 이 값들을 다 기억할 메모리도 문제지만 학습에 너무 많은 시간이 소요되기 때문에 사실상 학습이 불가능합니다. 앞에서 다뤘던 예제들도 다 gridworld같이 작은 예제였다는 것을 알 수 있습니다.
