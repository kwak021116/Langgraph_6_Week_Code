def show_messages(messages):
    """실제 반환된 메시지와 tool_calls만 표시합니다."""
    for index, message in enumerate(messages, 1):
        print(f'{index:02d}. {type(message).__name__}')
        if message.content:
            print('   내용:', message.content)
        for call in getattr(message, 'tool_calls', []):
            print('   도구 요청:', call['name'], call['args'])
            print('   요청 ID:', call['id'])
        if getattr(message, 'tool_call_id', None):
            print('   연결된 요청 ID:', message.tool_call_id)


def show_graph(graph):
    # 외부 이미지 렌더링 서비스에 접속하지 않고 연결 정보를 출력합니다.
    drawing = graph.get_graph()
    print('노드:', ', '.join(drawing.nodes))
    for edge in drawing.edges:
        suffix = ' [조건부]' if edge.conditional else ''
        print(f'{edge.source} -> {edge.target}{suffix}')


def show_mermaid(graph):
    """현재 그래프와 일치하는 Mermaid SVG를 로컬에서 표시합니다."""
    from pathlib import Path
    import hashlib
    from IPython.display import SVG, display

    source = graph.get_graph().draw_mermaid()
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]
    path = Path(__file__).resolve().parents[1] / "graphs" / f"{digest}.svg"

    if path.is_file():
        display(SVG(filename=str(path)))
    else:
        print("그래프 구조가 바뀌어 저장된 도식과 일치하지 않습니다.")
        print("아래 Mermaid 소스로 새 도식을 만들 수 있습니다.")
        print(source)
