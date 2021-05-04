# REST

: **Re**presentational **S**tate **T**ransfer

자원을 이름으로 구분 -> 해당 자원의 정보 주고 받음

HTTP URI(리소스의 고유 값)로 리소스 명시, HTTP Method(CRUD)로 자원 조작

#### CRUD

**C**reate(POST)

**R**ead(GET)

**U**pdate(PUT)

**D**elete(DELETE)



- Client -> Server: URI로 자원 지정, 조작 요청
- Server -> Client: 응답



#### 특징

1. Server-Client
2. Stateless
   - client의 context(세션, 쿠키 등)을 서버에 저장x
   - 서버는 모든 요청을 완전히 별개로 인식. 요청간의 처리에 연관성 없어야 함.
3. Cacheable
   - HTTP 프로토콜 그대로 사용 = 웹 기존 인프라 그대로 활용 가능 = HTTP의 캐싱 기능 적용 o
4. Layered System
   - Client는 REST API 서버만 호출. 서버는 다중 계층 구성 o
5. Code-On-Demand(optional)
   - 어떻게 처리해야 하는지에 대한 코드를 서버로부터 받아 클라이언트에서 실행
6. Uniform Interface
   - URI로 지정한 자원에 대한 조작을 통일되고 한정적인 인터페이스로 수행



# REST API

: REST 기반 서비스 API(프로그램들의 상호작용 돕는 매개체)

*ex*

**POST **/resource

**GET** /resource/:id

**PUT** /resource/:id

**DELETE** /resource/:id



# RESTful

: REST를 구현하는 웹. REST API를 제공하는 웹 = RESTful하다. REST 원리를 따르는 시스템

*ex*

CRUD를 모두 GET으로만 처리하는 API -> RESTful하지 않음

URI에 resource, id 외에 동사 표현/HTTP Method 등이 들어간 경우 -> RESTful 하지 않음