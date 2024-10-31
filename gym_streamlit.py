import requests
import streamlit as st

# Function to classify text using machine learning model
def classify(text):
    key = "855c2f80-974a-11ef-994e-b7bbb9cee7dd3f557c69-a989-488a-bf54-6c91a648996d"
    url = "https://machinelearningforkids.co.uk/api/scratch/" + key + "/classify"
    response = requests.get(url, params={"data": text})

    if response.ok:
        responseData = response.json()
        return responseData[0]  # Return top match
    else:
        response.raise_for_status()

# Streamlit interface for input
qu = st.text_input('오늘은 어디를 조지고 싶으신가요? (종료하려면 "종료" 입력) >> ')

if qu:
    if qu.lower() == "종료":
        st.write("프로그램을 종료합니다.")
    else:
        demo = classify(qu)
        label = demo["class_name"]
        confidence = demo["confidence"]

        if confidence < 50:
            st.write('질문을 이해하지 못했어요. 다시 질문해주세요')
        elif label.lower() == "arms":
            st.write('바벨 컬, 덤벨 컬, 해머 컬, 프리처 컬, 케이블 컬, 트라이셉스 익스텐션, 딥스, 푸시다운, 클로즈 그립 벤치프레스, 오버헤드 트라이셉스 익스텐션')
        elif label.lower() == "shoulder":
            st.write('오버헤드 프레스, 사이드 레터럴 레이즈, 프론트 레이즈, 리어 델트 플라이, 페이스 풀')
        elif label.lower() == "back":
            st.write('풀업, 바벨 로우, 랫 풀다운, 시티드 케이블 로우, 덤벨 로우')
        elif label.lower() == "legs":
            st.write('스쿼트, 레그 프레스, 런지, 레그 익스텐션, 카프 레이즈')
        elif label.lower() == "chest":
            st.write('벤치프레스, 인클라인 벤치프레스, 덤벨 플라이, 푸쉬업, 체스트 머신 플라이')

        st.write("result: '%s' with %d%% confidence" % (label, confidence))
