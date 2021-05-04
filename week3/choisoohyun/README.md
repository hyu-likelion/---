# REST vs REST API vs RESTful

# REST

---

'Representational State Transfer'의 약자

**자원**을 **표현으로 구분**하여 **상태를 주고 받는** 모든 것

- 자원: 해당 소프트웨어가 관리하는 모든 것
- 자원의 표현: 그 자원을 표현하기 위한 이름
- 상태 전달: 데이터가 요청되는 시점의 자원의 상태를 전달

'분산 하이퍼 미디어 시스템'(ex. 월드와이드 웹(www))을 위한 소프트 웨어 개발 아키텍처의 한 형식

- REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용 → 웹의 장점을 최대한 활용할 수 있음
- REST는 네트워크 상에서 Client와 Server 사이의 통신 방식 중 하나

**멀티 플랫폼에 대한 지원**을 위해 서비스 자원에 대한 아키텍처를 세우고 이용하는 방법을 모색한 결과, REST에 관심을 가지게 되었다.

### REST 특징

1. Server-Client(서버-클라이언트 구조)
2. Stateless(무상태)
3. Cacheable(캐시 처리 가능)
4. Layered System(계층화)
5. Code-On-Demand(optional)
6. Uniform Interface(인터페이스 일관성)

# REST API

---

API(Application Programming Interface): 데이터와 기능의 집합을 제공하여 컴퓨터 프로그램간 상호작용을 촉진하며, 서로 정보를 교환가능 하도록 하는 것

REST 기반으로 서비스 API를 구현한 것

REST는 HTTP 표준을 기반으로 구현하므로, HTTP를 지원하는 프로그램 언어로 클라이언트, 서버를 구현할 수 있다.

# RESTful

---

RESTful은 일반적으로 REST라는 아키텍처를 구현하는 웹 서비스를 나타내기 위해 사용되는 용어이다.

‘REST API’를 제공하는 웹 서비스를 ‘RESTful’하다

REST 원리를 따르는 시스템은 ‘RESTful’하다

### RESTful의 목적

이해하기 쉽고 사용하기 쉬운 REST API를 만드는 것

성능 향상보다는 API의 이해도 및 호환성을 높이는 것이 주 목적 → 성능이 중요한 상황에서는 굳이 RESTful한 API를 구현할 필요는 없다.
