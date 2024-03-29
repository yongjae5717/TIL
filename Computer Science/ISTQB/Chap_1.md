## 테스팅 지식 체계 목차(ISTQB)
#### 이 마크다운 파일은 개인적인 공부를 하기 위해 제작되었습니다.

---
### 공부 참고 사이트
- [실라버스](http://www.kstqb.org/board_skin/board_list.asp?bbs_code=4)
- [김기태의 JAVA를 자바](https://www.youtube.com/@java0405)

---
### Chap 1. 테스팅 기초
### Chap 2. SW 수명주기와 테스팅
### Chap 3. 정적 테스트 기법
### Chap 4. 테스트 설계 기법
### Chap 5. 테스트 관리
### Chap 6. 테스팅 지원 도구

---
####  K1, K2, K3, K4 (실라버스 내용 분배 각 34%, 59%, 6%, 1%)
- K1: Remember
- K2: Understand
- K3: Apply
- K4: Analyze

---
### ISTQB 문제 배분

|문제|CH.1|CH.2|CH.3|CH.4|CH.5|CH.6|Total|
|---|---|---|---|---|---|---|---|
|Foundation|7|6|3|12|8|4|40|

---
### 테스팅 용어
- [ISTQB 용어](http://dic.sten.kr/)

---
## 1. 소프트웨어 테스팅의 기초
### 의미 정리
<details>
<summary> 더보기 </summary>
<div markdown="1">

- **커버리지**: 특정한 커버리지 항목이 테스트 스위트에 의해 이행되는 백분율 정도
- **디버깅**: 소프트웨어에서 장애의 원인을 발견하고, 분석하여 제거하는 절차
- **결함**: 필요한 기능을 수행하지 못하도록 하는 컴포넌트나 시스템 상의 결점. 결함의 예는 부정확한 구문이나 부정확한 데이터 정의 등이다. 실행 중에 결함이 발생할 경우, 컴포넌트나 시스템의 장애를 야기할 수 있다.
- **오류**: 부정확한 결과를 초래하는 인간의 활동.
- **장애**: 컴포넌트나 시스템이 예상된 인도(delivery)나 서비스 또는 예상 결과와 실제적인 편차를 보이는 것
- **품질**: 컴포넌트, 시스템 또는 프로세스가 명시된 요구사항과 사용자/고객의 필요와 기대를 충족시키는 정도
- **품질 보증**: 품질 요구사항이 충족될 것이라는 신뢰감을 제공하는 데에 집중하는 품질 관리의 한 부분
- **근본 원인**: 불일치를 유발하는 근원적인 요소, 이것은 프로세스 개선을 통해 영구적으로 제거할 수 있다
- **테스트 분석**: 
- **테스트 베이시스**: 요구사항을 내포하고 있는 모든 문서. 테스트 케이스는 테스트 베이시스를 토대로 만들어 진다. 문서가 오직 공식적 수정 절차의 방법에 의해 수정될 수 있다면, 해당 테스트 베이시스를 동결 테스트 베이시스라 부른다.
- **테스트 케이스**: 특별한 목표 또는 테스트 상황을 테스팅하기 위해 개발된 입력값, 실행 사전조건, 예상 결과, 실행 사후조건 들의 집합
- **테스트 완료**: 
- **테스트 컨디션**:
- **테스트 제어**: 테스트 프로젝트에 계획 대비 차이가 나타나면 계획대로 진행되도록 정정 행동을 전개하고 적용하는 테스트 관리 업무. 테스트 관리 참고
- **테스트 데이터**: 테스트가 실행되기 이전에 테스트베이스와 같은 곳에 존재하며 테스트 대상 컴포넌트나 시스템에 영향을 주거나 영향을 받는 데이터
- **테스트 설계**: 테스트 아이템의 테스트 상황(커버리지 항목)과 상세한 테스트 접근법을 명세화하고 이와 연계된 상위 수준 테스트 케이스를 식별하는 활동
- **테스트 실행**: 
- **테스트 실행 일정**: 테스트 절차의 실행을 위한 계획. 테스트 실행 관련 정황과 실행될 순서를 고려하여 작성된 테스트 실행 일정은 테스트 절차를 포함한다
- **테스트 구현**:
- **테스트 모니터링**: 테스트 프로젝트의 상태를 정기적으로 점검하는 것과 관련된 활동을 다루는 테스트 관리 업무. 리포트는 실제(결과)를 계획된 것과 비교하여 준비된다
- **테스트 대상**: 테스트되는 컴포넌트나 시스템. 테스트 아이템 참고.
- **테스트 목적**: 테스트를 설계하고 실행하기 위한 근거 또는 목적
- **테스트 오라클**: 테스트 대상 소프트웨어의 실제 결과와 비교할 목적으로 예상 결과를 결정하는 근거 테스트 오라클은 기존 시스템, 사용자 메뉴얼, 또는 개인의 전문 지식일 수 있으나 코드(code)가 될 수는 없다.
- **테스트 계획**: 의도된 테스트 활동의 범위, 접근법, 자원, 그리고 일정을 기술하는 문서. 테스트 계획은 다른 테스트 항목, 테스트 대상의 기능 및 특성, 테스팅 업무, 업무 담당 배정, 테스터의 독립성 정도, 테스트 환경, 사용할 테스트 설계 기법과 테스트 측정 기법, 선택의 근거, 그리고 긴급 대책을 요하는 모든 리스크를 식별한다. **테스트 계획은 테스트 기획 프로세스를 기록한 것이다**
- **테스트 프로세스**: 기본적인 테스트 프로세스는 테스트 기획, 명세, 실행, 기록 그리고 완료 여부의 점검으로 구성된다.
- **테스트 스위트**: 테스트 대상 컴포넌트나 시스템에 사용되는 여러 테스트 케이스의 집합. 테스트 스위트는 테스트 사후조건이 주로 다음 테스트를 위한 사전조건이 되는 테스트 케이스로 구성된다
- **테스팅**: 소프트웨어 제품과 관련 작업 산출물이 특정 요구명세를 만족하는지 결정하고, 목적에 부합하는지 입증하고 결함을 찾아내기 위해 해당 산출물을 계획, 준비, 평가하는 정적/동적인 모든 수명주기 활동으로 구성된 프로세스
- **테스트웨어**: 테스트를 계획, 설계, 실행하는 테스트 프로세스 동안 생성된 산출물. 테스트웨어는 테스팅에 사용되는 문서, 스크립트, 입력값, 예상 결과, 시작과 마무리 절차, 파일, 데이터베이스, 환경, 그리고 모든 추가적인 소프트웨어 또는 유틸리티를 포함한다.
- **추적성**: 요구사항과 이와 연관된 테스트에서와 같이 문서나 소프트웨어에서 연관된 항목을 식별하는 능력
- **밸리데이션**: 요구사항이 컴포넌트나 시스템을 특정하게 의도적으로 사용 또는 활용하는 것을 충족시키는지 조사에 의해서나 객관적인 증거 제공으로 확인하는 것
- **베리피케이션**: 명세된 요구사항이 충족되었는지를 조사에 의해서나 객관적인 증거 제공으로 확인하는 것

</div>
</details>

### 소프트웨어 결함의 원인
#### 소프트웨어 결함
- 오류(인간의 행위, 실수)
  - 코드 작성, 소프트웨어나 시스템 또는 문서 작성시 결함을 만드는 오류
- 결함(요구된 기능의 부정확한 처리를 말하며 이것으로 인해 고장 또는 장애를 발생시키는 원인)
  - 시간적인 압박, 복잡한 코드, 기반환경의 복잡성, 기술이나 시스템의 변경, 수많은 시스템 상호간의 연동
  - 결함은 장애의 원인
  - 그러나 모든 결함이 장애를 발생시키는 것은 아님
- 장애(코드에 존재하는 결함의 실행 또는 환경적 조건에 의해 부정확하게 처리되는 것)
  - 결함 + 환경적인 조건

![img.png](Image%2Fimg.png)

---
### SW개발, 유지보수, 운영 시 테스팅의 역할
#### 테스팅
- **개발 초기**의 **요구사항 분석단계**부터 리뷰와 정적분석을 통해 정적으로 시작 -> 각각의 개발단계에 대응하는 테스트 레벨별
- 컴포넌트, 통합 테스팅은 **개발 조직 중심**으로 수행
- 시스템이 갖춰진 이후의 테스팅은 **독립적인 테스트 조직** 중심
- 테스트 레벨에 따른 테스트
  - 소프트웨어 품질을 높이고, 결함 발생 가능성을 최소화
- 유지보수 활동으로 변경 및 단종되거나 환경이 변경
  - 변경된 환경에 대해 운영 테스팅(**리그레션 테스팅**)
  - 변경으로 인한 결함과 장애를 예방
- 계약상 요구조건 및 산업에 특화된 표준 만족

---
### 테스팅과 품질
#### 품질 특성 및 향상
- ISO/IEC 9126 소프트웨어 제품 품질
  - 기능성, 신뢰성, 사용성, 효율성, 유지보수성, 이식성 
  - **문제: 소프트웨어 제품 품질에서 필요한 것은?**
- 품질 향상 -> 테스팅이 결함을 찾아내고, 발견된 결함을 수정
- 품질 보증 (QA)
  - 이전 프로젝트를 통해 많은 테스트 경험과 정보 확보
  - 발견된 결함의 근본 원인 이해를 통해 프로세스 개선
  - 결함의 재발 방지
- 개발 표준이나 교육 훈련 그리고 결함 분석

---
### 테스팅, 얼마나 해야 충분한가?
#### 적정한 테스트 정도
- 리스크 수준을 고려
- 프로젝트 제약 사항
  - 기술적인 내용
  - 비즈니스
  - 제품
  - 프로젝트 리스크
  - 시간
  - 비용
- 테스트된 SW나 시스템을 다음 단계로 전달하는 데 있어 프로젝트 이해관계자들이 **릴리즈 결정**을 내릴 수 있도록 충분한 정보 제공

---
### 테스팅이란 무엇인가?
#### 테스팅
- 응용 프로그램 또는 시스템의 동작과 성능, 안정성이 사용자가 요구하는 수준을 만족하는지 확인하기 위해 결함을 발견하는 메커니즘
  - 정상 동작 여부 확인
  - 사용자의 기대 수준과 요구사항에 맞게 구현되고 동작하는지 확인
  - 개발 프로젝트의 리스크 정보를 정량적 수치로 의사결정권자에게 전달
- 초기 개발 산출물 -> 리뷰
- 테스트 케이스 작성 과정 (결함 예방 활동)
- 다양한 테스팅 활동

#### 테스팅의 일반적인 목적
- 남아있는 결함 발견
- 명세 충족 확인
- 사용자 및 비즈니스 요구 충족
- 결함 예방
- 품질 수준에 대한 자신감 획득과 정보 제공
- 비즈니스 리스크를 감수시키는 정보에 근간한 조언 제공
- 개발 프로세스 점검, 이슈 제기
- 논리적 설게의 구현 검증
- 시스템과 소프트웨어가 적절히 동작함을 확인

#### 관점에 따른 테스팅의 목적
- 개발과정: 결함을 찾고 수정하기 위해 가능한 많은 장애 상황 재연
- 인수 테스팅: 예상대로 시스템이 동작하는지 확인, 요구사항 확인
- 소프트웨어 품질: 출시하는 것의 리스크를 관련자에게 전달
- 유지보수 테스팅: 변경에 대한 새로운 결함의 유입을 확인 (반복 테스트)
- 운영 테스팅: 신뢰성 또는 가용성 같은 시스템 특성을 평가
- 테스팅은 문서의 리뷰와 함께 정적 분석에 의한 테스트 포함

#### 테스팅과 디버깅의 차이 ?
|내용| 설명                                 |
|---|------------------------------------|
|테스팅| 장애를 통한 결함을 발견하는 것(동적 테스팅) <테스터가 수행>|
|디버깅| 장애의 원인을 찾고, 분석하여 제거하는 개발 활동<개발자가 수행>|

---
### 테스팅 용어
![img_1.png](Image%2Fimg_1.png)

---
## 3. 테스팅의 일반적인 원리
### 1. 테스팅은 결함이 존재함을 밝히는 것
- 잠재적으로 존재하는 결함 줄임
- 그러나, 결함이 없다고 증명할 수는 없음

### 2. 완벽한 테스팅은 불가능
- 한 프로그램 내에 내부 조건이 많음
- 입력이 가질 수 있는 모든 값의 조합이 무수히 많음
- 이벤트 발생 시 발생 순서에 대한 조합도 무수히 많음
- 리스크에 따라 테스트 강도 높게 수행 -> 실제 완벽은 불가

### 3. 개발 초기에 테스팅 시작
- 개발의 시작과 동시에 테스트를 계획하고 전략적으로 접근
- 요구사항 분석서와 설계서 등의 개발 산출물 분석 후 테스트 케이스 도출

### 4. 결함 집중
- 대다수의 결함들은 소수의 특정 모듈에 집중되어 발생하는 경향을 보임
- 결함의 집중은 운영상의 장애를 초래
  - 복잡한 구조의 모듈
  - 다른 모듈과 다량의 상호작용을 하는 모듈
  - 개발 난이도가 높거나 최신 기술을 사용한 모듈
  - 크기가 큰 모듈
  - 경험이 미흡한 팀에서 개발한 모듈
  - 새롭게 개발한 모듈

### 5. 살충제 패러독스
- 동일한 테스트 케이스로 동일한 테스트를 반복하면 결함을 찾기 어려워짐
- 더 많은 결함을 찾기 위해서는 테스트 케이스를 정기적으로 리뷰하고 개선

### 6. 테스팅은 정황에 의존적
- 테스팅은 정황과 도메인에 따라 다르게 진행
- 모든 테스트에 적용되어야 하는 것
  - 테스트 프로젝트 기획
  - 표준적인 기법적용
  - 독립적인 테스트 환경
  - 효율적/효과적 테스트 팀 조직
  - 정식 리포팅 등

### 7. 오류-부재의 궤변
- 개발된 소프트웨어가 사용자 요구수준을 만족하지 않는다면 버그를 수정하는 것은 의미가 없음

---
## 테스트 프로세스의 기초
![img_2.png](Image%2Fimg_2.png)

#### 1. 테스트 계획 & 제어
- 리스크 분석
- 전략 수립
- 테스트 종료 조건
- 모니터링(리포팅)

#### 2. 테스트 분석 & 설계
- 테스트 베이시스 검토

#### 3. 테스트 구현 & 실행
- 테스트 프로시저 생성 및 우선순위 선정
- 테스트 케이스 최종 구현과 우선순위 선정

#### 4. 종료 조건 평가 & 결과 보고 작성
- 종료 조건의 달성 여부 평가
- 최종 테스트 보고서 작성

#### 5. 테스트 활동 마무리
- 산출물 확인
- 테스트 프로세스 평가(진단)

### 테스트 프로세스
#### 정의: 테스팅 관련 활동이 체계적으로 진행되어 의도된 테스트 목적과 목표를 달성할 수 있도록 테스팅의 구성 요소를 엮어주는 역할
- 테스트 베이시스: 계획 단계부터 필요 설계 시 반드시 요구
- 테스트 조직: 계획 단계부터 필요, 실행 단계에서 다수 인력 필요
- 테스트 전략
- 테스트 기법: 분석 및 설계 단계에서 필요
- 테스트 대상: SW는 가장 이른 시기 준비, 늦어도 실행 단계엔 필수
- 테스트 기반 설비 및 환경: 실행 단계 전에 구축

#### 체계적으로 발견된 결함과 관련 정보를 바탕으로 정량적으로 개발 프로젝트에 조언(분석한 리스크)을 제공

![img_3.png](Image%2Fimg_3.png)

---
### 테스트 계획과 제어
- 주요 활동
  - 테스트 목적/목표 및 대상 연구
  - 테스트 전략 개발
  - 테스트 완료 조건의 결정
  - 테스트를 추정
  - 테스트 조직 구성
  - 테스트 계획 활동
  - 테스트 관리 및 제어
  - 리포팅

---
### 테스트 제어
- 계획 대비 실제 진행 상황을 비교하는 지속적인 활동
- 계획과의 차이 확인 -> 지속적 모니터링
- 제어 작업
  - 테스트 결과에 대한 측정과 분석
  - 테스트 진척사항, 완료조건의 모니터링과 문서화
  - 테스트 계획과의 차이 교정
  - 테스팅의 진행과 변경에 대한 의사 결정 활동
  - 테스팅 계획은 테스팅의 제어와 모니터링 활동으로부터 받은 피드백을 반영


---
### 테스트 분석과 설계
- 일반적이고 추상적인 테스팅 목적을 실제적이고 구체적인 테스트 상황과 테스트 케이스로 변환하는 활동
- 주요 작업
  - 테스트 베이시스(ex, 요구사항 명세서) 리뷰
  - 테스트 상황 / 테스트 케이스 / 필요한 테스트 데이터 식별
  - 테스트 케이스 설계와 우선순위 선정
  - 테스트 기법 할당
  - 테스트 용이성 평가
  - 테스트 환경 구축 (실제 환경과 동일)
  - 필요한 도구 식별

---
### 테스트 구현과 실행
- 테스트 케이스를 조합하고 테스트 실행에 필요한 다른 정보를 포함하는 테스트 프로시저 또는 테스트 스크립트를 명세화
- 테스트에 필요한 환경이 구축되어야 함
- 주요 작업
  - 테스트 케이스 개발, 구현과 우선순위 설정
  - 자동화 테스트 스크립트 작성
  - 테스트 하네스(테스트를 수행하기 위해 필요한 스텁과 드라이버로 구성된 테스트 환경) 준비(환경)
  - 효율적인 테스트 실행을 위해 테스트 수트(테스트 케이스 묶음) 생성
  - 선행 테스트
  - 테스팅 실행(결과 기록 - 식별과 버전관리)
  - 기대 결과와 비교 -> 예상 결과와 실제 결과 간의 차이에서 오는 불일치를 인시던트 또는 결함으로 보고 -> 불일치 원인 파악
- 예상과 실제의 불일치
  - 테스트 케이스 결함
  - 테스트 정황 결함
  - 어플리케이션 결함
- 불일치를 조치한 결과를 확인하기 위한 테스트 활동 반복
  - 수정이 되었는지 테스트 실행 -> 확인 테스팅
  - 수정으로 새로운 버그가 발생하지 않았는지 테스트 실행 -> 회귀 퇴스팅(리그레션 테스팅)
- 결함의 유형
  - 기획 시 유입된 결함 - 요구사항의 표준 미준수, 테스트 불가능 등
  - 설계 시 유입된 결함 - 설계의 표준 미준수, 테스트 불가능 등
  - 코딩 시 유입된 결함 - 코드의 표준 미준수 등
  - 테스트 부족으로 유입된 결함
  - 마무리 부족
  - 팀간 의사소통 부족
  - 코딩 실수
- 결함 심각도에 따른 결함 유형
  - 치명적 결함, 매우심각, 심각, 보통, 경미
  - 치명적 결함, 주요 결함, 일반 결함, 사소한 결함, 개선사항
- 결함 유형으로 부적절한 경우
  - Major, Minor, Trifle
  - A, B, C
- 결함의 우선순위 표현
  - 즉시 해결, 주의 요망, 대기, 낮은 순위

---
### 테스트 완료조건의 평가
- 초기 목표 대비 완료조건의 달성 여부 확인
- 테스트 레벨에 따라 다 수행 함
- 완료 조건 작업
  - 테스트 실행 결과인 테스트 로그가 테스트 계획에 명시된 완료 조건을 만족하는지 확인
  - 추가 테스트 필요 여부 및 명세화된 테스트 완료 조건 변경 여부
  - 이해관계자들에게 배포할 테스트 요약 보고서 작성

---
### 리포팅에 표현되는 내용
- 발견된 결함 / 미해결된 결함의 추이 / 우선순위
- 테스트 진척도
- 리스크 및 메트릭으로 실증된 조건
- 테스트 환경의 가용성(다음에 사용 가능한지 여부)
  - 테스트 커버리지
  - 결함 발견 효율성/효과성
  - 품질 평가 보증
  - 결함상태별 결함수
  - 소프트웨어 사이즈 대비 결함수
  - 요구사항별 테스트 건수
  - 해결되지 않은 결함과 영향 및 오래 수정되지 않은 결함

---
### 테스트 마감 활동 
- 산출물 확인, 테스트웨어(산출물) 보관
- 테스트 프로세스 평가 심사
- 주요 활동
  - 테스트 결과 마감(문서화)
  - 테스트웨어, 테스트환경, 테스트기반설비를 차후에 사용하기 위해 마감, 보관
  - 테스트웨어 유지보수 조직에 이관
  - 테스트 프로세스 심사 및 개선 사항
  - 이후 릴리즈나 프로젝트, 테스트 성숙도의 개선에 지침이 될 수 있도록 테스트 프로젝트를 통해 얻은 교훈을 분석

---
## 테스팅의 심리학
### 개발자와 테스팅 엔지니어 분리 -> 각자의 활동에 집중
### 테스팅 독립성
- 테스트 대상 소프트웨어의 개발자가 설계한 테스트
- 개발팀 내의 다른 인원이 설계한 테스트
- 다른 그룹의 독립적인 테스트 팀의 인원 또는 테스트 전문가가 설계한 테스트
- 다른 조직 또는 다른 회사의 인원이 설계한 테스트
  - 명확한 테스팅의 목표 설정은 테스팅을 성공적으로 수행하는데 있어 중요

---
### 테스팅 진행하는 동안 결함을 식별하는 과정
- 작성자에 대한 비판으로 오해될 소지 존재
  - 호기심, 전문적인 비평, 비판적인 시선, 세밀한 것에 주목하는 태도, 개발자 또는 개발팀 동료와의 원활한 의사소통, 그리고 결함을 유추해 내는 경험 필요
- 오류나 결함, 장애가 긍정적인 방법으로 **의사소통** 된다면, 테스터와 개발자 간에 발생할 수 있는 **감정 악화**를 피할 수 있다.
- 테스터, 테스트 리더 사이
  - 좋은 **대인 관계**가 필요
- 결함 정보
  - 결함 발견 -> 시간과 비용 절감 및 리스크 요소 줄임

---
### 테스터의 역할
- 다툼보다는 협력으로 시작 -> 공통적인 목표를 모든 사람에게
- 소프트웨어를 개발한 사람에게 비평을 배제하고 중립적이고 사실에 근거한 제품의 결함만 전달하려고 노력한다
- 다른 인원이 어떻게 느끼는지, 왜 그렇게 반응하는지 이해하도록 노력한다
- 상화간에 의사소통 했던 것을 상대방이 정확하게 이해했는지 확인한다

---
### 최근 SW
- 전통직인 컴퓨팅 영역 탈피
  - 가전, 무선단말기, 산업기기, 휴대폰 자동차 분야
- SW 개발 프로세스 품질의 중요성과 함께 SW 결함에 사전에 진단하고 정상 작동여부를 시험하는 테스팅의 중요성 부각
  - 전체 개발비의 40% ~ 60% 이상이 **테스팅 비용**
  - 하지만 기존 개발자들은 테스팅에 소극적 -> 하위레벨 테스트 부족
- 품질에 대한 인식 높아져 기대 수준 높아짐 -> **리스크** 관리 필요
  - 체계적인 테스팅을 위해서는 테스트의 **우선순위** 중요

---
### 테스트에 대한 문제점
- 테스터가 테스팅에 대해 너무 단편적으로 알고 있는 것은 체계적인 테스팅을 제약하는 요인
  - 개념과 연관성 이해
  - 리스크 기반 테스팅 접근법 / 테스트 기법 / 테스트 커버리지
  - 이론을 실무에 적용하는 노력 필요
- 의사결정권자와 매니저의 테스팅에 대한 인식 부족
  - 임시방편
  - 테스트 자동화 도구의 중장기적 계획 또는 테스트 프로세스 정립 필요
- 테스팅을 투자가 아닌 불필요한 비용으로 인식
  - 테스팅은 개발보다 더 확실한 ROI(Return On Investment) 활동

---
### 테스팅 분야의 매력
#### 테스팅 분야의 전문가
- 체계적인 지식 체계를 갖는 전문 분야
  - 기존적인 컨셉과 테스트 전략, 계획 설계 기법, 테스트 케이스 작성 등의 분야
- 테스팅 분야는 넓고 다양함
  - 자동화 도구에 대한 전문적 기술
  - 보안성 테스트, 신뢰성 테스팅 분야 전문가
  - 테스팅 컨셉, 기법 및 관리 방법을 소프트웨어 종류별 최적화하여 적용
- 테스팅 필요성 급증
- 테스팅 분야에서 연령 제한 X, 경험 중시

---
### 테스트 전문가에 대한 수요
- 계속적으로 증가 -> 소비자의 품질에 대한 마인드와 기대수준이 높음
- 전문 인력 수급 어려움
- **능력있는 테스트 전문가**
  - 기술능력: 소프트웨어 공학 이해, 테스트 수행 능력
  - 개인 능력: 커뮤니케이션, 분석력, 문서화, 결함 유추
  - 습성: 충분한 이해와 도구 사용, 표준화 노력
  - 사고방식과 태도: 주인의식, 열정, 적극, 긍정, 호기심, 비판적인 시선 등
