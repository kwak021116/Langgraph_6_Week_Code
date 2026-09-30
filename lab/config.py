"""실습 루트의 .env를 읽습니다. 키를 출력하거나 코드에 저장하지 않습니다."""
from dataclasses import dataclass, field
from pathlib import Path
import os
from dotenv import dotenv_values

ROOT = Path(__file__).resolve().parents[1]

@dataclass(frozen=True)
class Settings:
    api_key: str = field(repr=False)
    model: str = 'gpt-4o-mini'
    timeout: float = 60.0
    server_url: str = 'http://127.0.0.1:2024'

def load_settings(env_path=None):
    path = Path(env_path) if env_path else ROOT / '.env'
    values = dotenv_values(path, encoding="utf-8-sig") if path.is_file() else {}
    def read(name, default=''):
        # 수업에서는 학생이 수정한 .env를 먼저 사용합니다.
        # 빈 값은 건너뛰고 환경변수, 기본값 순으로 확인합니다.
        for value in (values.get(name), os.environ.get(name), default):
            if value is not None and str(value).strip():
                return str(value).strip()
        return ""
    key = read('OPENAI_API_KEY')
    if not key or key.lower() in {'your-api-key', 'your_openai_api_key', 'sk-your-key-here'}:
        raise ValueError(
            f'OPENAI_API_KEY가 없습니다. {path} 파일의 OPENAI_API_KEY= 뒤에 본인 키를 넣으세요. '
            '설치 후 처음 실행한다면 .env.example을 .env로 복사하세요. 키를 노트북 셀에 붙여 넣지 마세요.'
        )
    model = read('OPENAI_MODEL', 'gpt-4o-mini')
    try:
        timeout = float(read('OPENAI_TIMEOUT', '60'))
    except ValueError:
        raise ValueError('OPENAI_TIMEOUT은 초 단위 숫자여야 합니다.') from None
    if not 0 < timeout < float('inf'):
        raise ValueError('OPENAI_TIMEOUT은 0보다 큰 유한한 숫자여야 합니다.')
    return Settings(key, model, timeout, read('LANGGRAPH_SERVER_URL', 'http://127.0.0.1:2024'))

def make_llm():
    from langchain_openai import ChatOpenAI
    settings = load_settings()
    return ChatOpenAI(model=settings.model, api_key=settings.api_key,
                      timeout=settings.timeout, max_retries=1)
