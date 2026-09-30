# Module 1 페이지별 실습

발표 PDF 17개 페이지에 대응하는 독립 실행 노트북입니다. 데모 모델은 없으며 모델을 사용하는 실습은 실제 OpenAI API를 호출합니다. 그래프 기초 실습은 원래 LLM이 필요하지 않으므로 키 없이 실행됩니다.

## 빠른 시작

```bash
git clone https://github.com/kwak021116/Langgraph_6_Week_Code.git
cd Langgraph_6_Week_Code
```

Python 3.11 이상(검증 환경: Python 3.12)을 사용하세요. 터미널의 현재 위치를 이 폴더로 옮깁니다.

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows PowerShell
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
PowerShell에서 활성화가 막히면 정책을 변경할 필요 없이 `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`처럼 해당 Python을 직접 실행할 수 있습니다.

## API 키 입력

`.env.example`을 `.env`로 복사한 뒤 본인의 API 키를 입력하세요.

```dotenv
OPENAI_API_KEY=본인의_API_키
OPENAI_MODEL=gpt-4o-mini
OPENAI_TIMEOUT=60
LANGGRAPH_SERVER_URL=http://127.0.0.1:2024
```

`lab/config.py`가 Python dotenv로 읽습니다. **프로세스 환경변수가 .env보다 우선**합니다. 설정을 바꾼 뒤 모델 생성 셀부터 다시 실행하세요. 키가 없으면 모델 실습에서 안내 오류가 발생합니다. 키를 공유하거나 노트북 출력에 넣지 마세요. 계정에서 사용 가능한 tool calling 지원 모델로 모델명을 변경할 수 있습니다. API 요청은 유료 사용량을 발생시킵니다.

## Jupyter 실행
```bash
python -m ipykernel install --user --name module1-lab --display-name "Python (Module 1)"
python -m jupyterlab
```
노트북에서 **Python (Module 1)** 커널을 선택하세요. `ipynb/01_시작하기.ipynb`부터 엽니다. VS Code에서는 `.venv`의 Python을 커널로 직접 선택해도 됩니다. 각 파일을 위에서 아래로 실행하며 파일 간 선행 실행은 필요 없습니다.

## 페이지 대응표

| PDF 쪽 | 노트북 | API 키 |
|---|---|---|
| 1 | [환경 확인과 학습 목표](ipynb/01_시작하기.ipynb) | 불필요 |
| 2 | [Workflow와 Agent](ipynb/02_workflow_agent.ipynb) | 필요 |
| 3 | [State, Node, Edge](ipynb/03_state_node_edge.ipynb) | 불필요 |
| 4 | [그래프의 설계와 실행](ipynb/04_compile_invoke.ipynb) | 불필요 |
| 5 | [일반 edge와 조건부 edge](ipynb/05_conditional_edge.ipynb) | 불필요 |
| 6 | [State 업데이트와 Reducer](ipynb/06_reducer.ipynb) | 불필요 |
| 7 | [대화 메시지와 MessagesState](ipynb/07_messages_state.ipynb) | 불필요 |
| 8 | [Tool binding과 실제 실행](ipynb/08_tool_binding.ipynb) | 필요 |
| 9 | [Module 1의 Chain](ipynb/09_chain.ipynb) | 필요 |
| 10 | [Module 1의 Router](ipynb/10_router.ipynb) | 필요 |
| 11 | [Agent와 ReAct](ipynb/11_agent.ipynb) | 필요 |
| 12 | [연속 도구 호출 예시](ipynb/12_multi_tool.ipynb) | 필요 |
| 13 | [실행 중 State와 여러 호출에 걸친 Memory](ipynb/13_without_memory.ipynb) | 필요 |
| 14 | [Checkpointer와 thread_id](ipynb/14_checkpointer.ipynb) | 필요 |
| 15 | [Memory 비교 시연](ipynb/15_memory_comparison.ipynb) | 필요 |
| 16 | [LangGraph, API, Studio, SDK, Deployment](ipynb/16_ecosystem.ipynb) | 불필요 |
| 17 | [로컬 실행과 SDK의 흐름](ipynb/17_server_sdk.ipynb) | 필요 |

## 발표 시연 추천

- 3쪽: c만 반환해도 a, b가 유지되는지 질문하고 결과 확인
- 5쪽: c=30의 분기 결과 예측
- 6~7쪽: 리스트 결합과 메시지 ID 갱신 비교
- 9~11쪽: 마지막 메시지 종류와 tools 이후 연결 비교
- 12쪽: 실제 도구 인자와 결과, assistant 호출 횟수 확인
- 13~15쪽: 최종 답변 문구 대신 이전 메시지 포함 여부로 메모리 확인
- 17쪽: 별도 터미널의 로컬 서버 필요. 설치/실행법은 노트북 첫 설명 참조

## 결과와 반복 실행

GitHub에 올린 노트북은 실행 출력을 비워 두었습니다. API 호출 노트북에도 실제로 실행하지 않은 응답을 만들어 넣지 않았습니다. 본인 키로 실행하면 결과가 각 셀 아래에 표시됩니다. 모델 응답의 문구·도구 선택·호출 횟수는 슬라이드의 대표 예시와 다를 수 있습니다.

메모리 실습은 같은 graph와 thread로 반복 실행하면 대화가 누적됩니다. 처음부터 비교하려면 커널을 재시작하거나 graph 생성 셀부터 실행하세요. 기본 재시도는 1회, 요청 timeout은 60초입니다. 인증 오류는 키, 사용량 오류는 계정 한도, 모델 오류는 OPENAI_MODEL을 확인하세요.

## 검증 범위

17개 노트북의 문법과 구조를 확인했고, 1·3·4·5·6·7·16쪽은 실행 결과를 검증했습니다. 라이브 API와 로컬 Agent Server 요청은 검증하지 않았습니다. 본인 API 키로 실행해 확인하세요.

## 출처

사용자 발표 PDF 「지능형자동화실습 6주차 발표자료」와 LangChain Academy module-1의 simple-graph, chain, router, agent, agent-memory, deployment 노트북을 기준으로 구성했습니다.
- https://github.com/langchain-ai/langchain-academy/tree/main/module-1
- https://docs.langchain.com/oss/python/langgraph/graph-api
- https://docs.langchain.com/oss/python/langgraph/persistence
- https://docs.langchain.com/langsmith/local-dev-testing

## 쉬운 예시로 다시 구성한 버전

- 기존 apps_강의자료.pptx의 a=10, b=20, c/d/e 계산을 사용합니다.
- 조건 분기는 기존 PPT의 node1/node2/node3와 large/small을 사용합니다.
- reducer는 기존 PPT의 첫 번째/두 번째 events 예시입니다.
- operator.add와 add_messages는 같은 메시지 ID를 사용하고 각 예제를 별도 셀로 끝까지 실행합니다.
- 덧셈/곱셈 도구는 노트북 안에 직접 정의합니다.
- 함수/분기 내부는 공백 4칸 들여쓰기입니다. 한 줄 함수, 삼항식, 그래프 등록용 반복문을 사용하지 않습니다.
- 메모리 비교도 A/B/C를 별도 구역에서 실행합니다.
- 결과 해설은 예상/대표 결과입니다. 실제 API 응답은 실행 후 셀 아래에서 확인합니다.
