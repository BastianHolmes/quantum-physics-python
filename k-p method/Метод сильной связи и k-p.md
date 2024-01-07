### k-p метод
Уравнение Шредингера 
$$[\frac{\vec{p}^2}{2m}+U(\vec{r})]|\Psi(\vec{r})=E\Psi(\vec{r})$$
раскладывается вблизи интересующей точки экстремума зон $\vec{K_0}$ в базисе блоховских функций $\psi_n\vec{k_0}$, т.е. решение записывается в виде:
$$\Psi_k(\vec{r})=e^{i\vec{k}r}\sum_nc_n\psi_{nK_0}(\vec{r})$$
$$\psi_{nK_0}(\vec{r})=e^{iK_0\vec{r}}u_n(\vec{r})$$
Здесь n нумерует зоны, которые  учитываются в рассмотрении, а $u_n(\vec{r})$ - блоховские амплитуды.
Если подставить разложение в уравнение Шредингера, то надо протащить функции, через оператор импульса $\vec{p}=-i\hbar\nabla$ получим
$$[\frac{\vec{p^2}}{2m}+u(\vec{r})]\psi_{nK_0}(\vec{r})=E_n(K_0)\psi_{nK_0}(\vec{r})$$
Если дальше преобразовывать уравнение, можно получить матричный вид:
$$\sum_n[(E_{n'}(K_0)+\frac{\hbar^2k^2}{2m})\delta_{nn'}+\frac{\hbar}{m}k\cdot p_{nn'}]c_{n'}=E_n(k)c_n$$
Здесь $p^\alpha_{nn'}=\int\psi*_{nK_0}\hat{p}^\alpha\psi_{n'k_0}dV$
Тогда во втором порядке теории возмущений по оператору $k\cdot p^\alpha_{nn'}$ можно записать
$$E_n(k)=E_n(K_0)+\frac{\hbar}{m}\sum_\alpha k_\alpha p^\alpha_{nn'}+\sum_{\alpha\beta}\frac{\hbar^2}{2m_{\alpha\beta}}k_\alpha k_\beta$$
Здесь 
$$\frac{1}{m_{\alpha\beta}}=\frac{1}{m}\delta_{\alpha\beta}+\frac{1}{m^2}\sum_{n'}\frac{p^\alpha_{nn'}p^\beta_{n'n}+p^\beta_{nn'}p^\alpha_{n'n}}{E_n(K_0)-E_{n'}(K_0)}$$
### Метод сильной связи
Метод сильной связи состоит в том, что волновые функции записываются в виде разложения по локализованным на атомах функциям.
$$\psi(\vec{r})=\sum_{n,\alpha}C_{n,\alpha}\Phi_\alpha(\vec{r}-\vec{R_n})$$
Здесь $\alpha$ нумерует орбитали, n нумерует атомы с координатами $R_n$
Подставляя в уравнение Шредингера получаем уравнение на собственные числа:
$$\sum H_{n\alpha,n'\beta}C_{n'\beta}=E\sum S_{n\alpha, n'\beta}C_{n'\beta}$$
Это задача решается ортогонализацией Левдина.
### Зонная структура графена
Решётка:
$\vec{a}_1=\frac{\sqrt a}{2}(1, \sqrt3)$
$\vec{a}_2=\frac{\sqrt a}{2}(-1, \sqrt3)$
Обратная решётка:
$\vec{b}_1=\frac{2\pi}{3a}(\sqrt3,-1)$
$\vec{b}_2=\frac{2\pi}{3a}(\sqrt3,1)$
В итоге получается гамильтониан:
$H=h\cdot\sigma$ 
$h_x(k)=-t\sum_{n=1}^3cos k \cdot \delta_n$
$h_y(k)=-t\sum_{n=1}^3sin k \cdot \delta_n$
$h_z(k)=0$
В явном виде:
$$H=\left(\begin{array}{cc} 
0 & tf(k)\\
tf^*(k) & 0 
\end{array}\right)$$
$f(k)=e^{ik_ya}+2e^{-ik_ya/2}cos(\frac{sqrt3}{2}k_xa)$ 
В точках $K_0=(\frac{4\pi}{3\sqrt3a}, 0), K'_0=-K_0$ энергия зануляется и вырождается, дисперсия в окрестности оказывается линейной $h(k)=v_Fq\cdot\sigma$ 

