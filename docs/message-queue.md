# Message Queue 

## RabbitMQ
- 오픈소스 메시지 브로커 
- AMQP(Advanced Message Queuing Protocol) 표준을 따른다
- 비동기 처리, 메세지 queue, 마이크로 서비스 간 통신
- 활용
  - 메시지를 많은 사용자에게 전달
  - 요청에 대한 처리 시간이 길 때
  - 해당 요청을 다른 API에 위임하고 빠른 응답을 할 때

## RabbitMQ 개념
1. Producer
   - 메시지를 생성하고 발송하는 주체
   - producer가 생성하는 메시지는 Exchange를 거쳐 Queue에 저장
2. Consumer
   - 메시지를 수신하는 주체
   - Queue에 직접 접근하여 메시지를 가져온다
3. Queue
    - Producer들이 발송한 메시지들이 Consumer가 소비하기 전까지 보관되는 장소
4. Exchange
    - Producer들에게서 전달받은 메시지들이 어떤 Queue에 발송할지를 결정하는 객체
5. Binding
    - Exchange에게 메시지를 라우팅할 규칙을 지정하는 행위
    - 특정 조건에 맞는 메시지를 특정 Queue에 전송할 수 있도록 설정
    - Exchange:Queue = m:n

### Exchange Type
1. Direct : [Unicast] Routing Key가 정확히 일치하는 큐에 전송
2. Topic : [Multicast] Routing Key 패턴이 일치하는 큐에 전송
3. Headers : [Multicast] 키:밸류 로 이루어진 헤더 기준으로 일치하는 큐에 전송
4. Fanout : [Broadcast] 해당 Exchange에 등록된 모든 큐에 전송
