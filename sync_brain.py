import os

# 1. NotebookLM에 기억시킬 글로벌 핵심 인프라 자재 명단
TARGET_FILES = [
    "_quarto.yml",
    "styles.css",
    "template_blueprint.qmd",  # 인터랙티브 앱 및 테이블 뼈대 양식
    "index.qmd",               # 루트 메인
    "investment/index.qmd",    # 투자 메인
    "hobbies/index.qmd",       # 취미 메인
    "gallery/index.qmd"        # 갤러리 메인
]

def execute_brain_sync():
    # 🌟 다른 외각 경로를 배제하고, 현재 Quarto 프로젝트 루트에 정식 파일 지정
    output_target = "Quarto_AI_Brain.txt"

    combined_raw_data = "# QUARTO BLOG GLOBAL ARCHITECTURE BLUEPRINT\n"
    combined_raw_data += "⚠️ WARNING: 이 문서는 AI 컨텍스트 주입용 동기화 원장입니다. 각 파일의 경로 식별자를 확인하여 해석하십시오.\n\n"
    
    for relative_path in TARGET_FILES:
        if os.path.exists(relative_path):
            # 파일별 고유 경로 메타데이터 태그 락인 (이름 충돌 원천 차단)
            combined_raw_data += f"\n\n=========================================\n"
            combined_raw_data += f"📂 [FILE NODE PATH]: /{relative_path}\n"
            combined_raw_data += f"=========================================\n\n"
            
            with open(relative_path, "r", encoding="utf-8") as f:
                combined_raw_data += f.read()
                
            combined_raw_data += f"\n\n/* END OF NODE: /{relative_path} */\n"
            print(f"textCopy✅ {relative_path} 자재가 원장에 정밀 적재되었습니다.")
        else:
            print(f"⚠️ 경고: {relative_path} 경로를 찾을 수 없어 배관에서 제외합니다.")
            
    # 로컬 파일로 다이렉트 사출
    with open(output_target, "w", encoding="utf-8") as out_f:
        out_f.write(combined_raw_data)
        
    print(f"\n🏁 [공정 완공] 프로젝트 루트에 통합 원장이 성공적으로 마감되었습니다.")
    print(f"📍 생성 위치: {os.path.abspath(output_target)}")

if __name__ == "__main__":
    execute_brain_sync()