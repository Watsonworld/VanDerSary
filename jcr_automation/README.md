# JCR 자동화 작업 환경

이 폴더를 **VS Code의 프로젝트 폴더**로 열고, Obsidian에서는 같은 폴더를 **Vault**로 연다. Obsidian에서 `notes/00-시작.md`를 열면 원문 명세와 체크리스트로 이동할 수 있다. Markdown 저장만으로 AI 코드가 자동 생성되지는 않는다. VS Code의 Codex 확장에서 `notes/구현-체크리스트.md`의 작업 요청을 보내면, Codex가 문서를 읽고 코드를 생성·실행한다.

## 최초 설정

1. VS Code에 Python 확장과 Codex 확장을 설치하고 로그인한다. Obsidian도 설치한다.
2. 이 폴더(`jcr_automation`)를 두 앱에서 연다. Obsidian에는 새 Vault를 만들지 말고 **기존 폴더를 Vault로 열기**를 선택한다.
3. `input/article_list.xlsx`에 논문 파일을 넣는다. 공식 JCR Export는 `input/jcr/`에 넣는다. 두 파일은 Git에서 제외된다.
4. VS Code에서 **Terminal → Run Task → JCR: set up Python**을 실행한다. Windows에서는 Python 인터프리터를 `.venv/Scripts/python.exe`로 선택한다. 터미널에서도 설치할 수 있다.

```powershell
py scripts/setup_env.py
```

5. Codex 채팅에 `notes/구현-체크리스트.md`의 작업 요청을 붙여 넣는다. 먼저 실제 파일 분석 결과를 확인하고 이후 구현을 진행한다.

## 구현 후 월별 실행

`JCR: run monthly report` 작업을 사용한다. Windows 터미널에서는 다음을 실행할 수도 있다.

```powershell
.venv\Scripts\python.exe main.py
```

교수·Category 검색은 구현 후 `python main.py --professor "김병인"`, `python main.py --category "Operations Research & Management Science"` 형태로 사용한다. 결과는 `output/`에 저장한다.

현재 입력 Excel과 공식 JCR Export가 아직 없어서 `main.py`와 실제 결과 파일은 생성되지 않았다.
