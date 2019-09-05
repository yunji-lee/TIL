# 데이터 로드
library(ggplot2)
data("diamonds")
head(diamonds)

# 1 기본 그래픽스

# 기본 히스토그램
hist(diamonds$carat, main = 'Carat Historam', xlab = 'Carat')

# 기본 산점도
plot(price ~ carat, data = diamonds)
plot(diamonds$carat, diamonds$price)

# 상자그림
boxplot(diamonds$carat)


# 2 ggplot2

# 2.1 히스토그램과 밀도곡서
# 히스토그램
ggplot(data = diamonds) + geom_histogram(aes(x = carat))
# 밀도곡선
ggplot(data = diamonds) + geom_density(aes(x = carat), fill = 'grey50')


# 2.2 산점도
# 산점도
ggplot(diamonds, aes(x = carat, y = price)) + geom_point()
# ggplot(diamonds) + geom_point(aes(x = carat, y = price))
ggplot(diamonds, aes(x = carat, y = price)) + geom_point(aes(color = color))
ggplot(diamonds, aes(x = carat, y = price)) + geom_point(aes(color = color)) + facet_wrap(~color)
ggplot(diamonds, aes(x = carat, y = price)) + geom_point(aes(color = color)) + facet_grid(cut~clarity)


# histogram faceting
ggplot(diamonds, aes(x = carat)) + geom_histogram() + facet_wrap(~color)

# 2.3 상자그림과 바이올린 플롯
# 상자그림
ggplot(diamonds, aes(y = carat, x =1)) + geom_boxplot()
ggplot(diamonds, aes(y = carat, x =cut)) + geom_boxplot()
# 바이올린 플롯
# 상자그림과 바이올린 플롯
# 상자그림
ggplot(diamonds, aes(y = carat, x =cut)) + geom_violin()
ggplot(diamonds, aes(y = carat, x =cut)) + geom_point() + geom_violin()
ggplot(diamonds, aes(y = carat, x =cut)) + geom_violin() + geom_point()


# 2.4 꺾은선그래프
ggplot(economics, aes(x = date, y = pop)) + geom_line()


# lubridate 패키지 로딩
# install.packages('lubridate')
library(lubridate)

# year, month 변수 생성
economics$year <- year(economics$date)
# 다음 label 인자는 월을 숫자가 아닌 이름으로 반환하게 한다.
economics$month <- month(economics$date, label = TRUE)

# 데이터 서브세팅
# 조건이 참인 경우에 해당하는 인덱스를 반환한다. 2000년 이후의 데이터를 가져온다.
econ2000 <-  economics[which(economics$year >= 2000),]

# 축 포맷팅을 위해서 scales 패키지를 로딩
library(scales)

# 플롯의 초기화
g <- ggplot(econ2000, aes(x = month, y = pop))
# 선들을 색으로 코드화하고, year에  따라 그룹화한다.
# group 에스테틱은 데이터를 별도의 그룹으로 세분한다.
g <- g + geom_line(aes(color = factor(year), group = year))
# 레전드의 이름을 year로 한다.
g <- g + scale_color_discrete(name = 'year')
# y축 포맷
g <- g + scale_y_continuous(labels = comma)
# 제목과 축 레이블 추가
g <- g + labs(title = 'Population Growth', x = 'Month', y = Population)
# 플롯을 출력
g

# 2.5 테마
library(ggthemes)
# 플롯을 만들어 g2에 저장
g2 <- ggplot(diamonds, aes(x = carat, y = price)) + geom_point(aes(color = color))
# 테마 설정
g2 + theme_economist() + scale_color_economist()
g2 + theme_excel() + scale_color_excel()
g2 + theme_tufte()
g2 + theme_wsj()
