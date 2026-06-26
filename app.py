import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="배사메무초 영어학원 홍보 카피", layout="centered")
st.title("📣 배사메무초 영어학원 — 3채널 홍보 카피")
st.caption("여름방학 특강 · 조기등록 20% 할인 · 초등 6학년 중등 선행반")

html_content = """
<style>
  body { font-family: sans-serif; margin: 0; padding: 0; }
  .wrap { padding: 1rem 0; display: flex; flex-direction: column; gap: 1.5rem; }
  .card { background: #fff; border: 1px solid #e0e0e0; border-radius: 12px; overflow: hidden; }
  .card-header { display: flex; align-items: center; gap: 10px; padding: 0.75rem 1.25rem; border-bottom: 1px solid #e0e0e0; background: #fafafa; }
  .badge { font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; }
  .blog-badge { background: #e3f2fd; color: #1565c0; }
  .insta-badge { background: #fce4ec; color: #880e4f; }
  .kakao-badge { background: #fff9c4; color: #795548; }
  .channel-label { font-size: 14px; font-weight: 600; color: #111; }
  .char-count { margin-left: auto; font-size: 12px; color: #999; }
  .card-body { padding: 1.25rem; position: relative; }
  .card-body p { font-size: 14px; line-height: 1.9; color: #222; margin: 0; white-space: pre-line; }
  .tags { margin-top: 0.75rem; display: flex; flex-wrap: wrap; gap: 6px; }
  .tag { font-size: 12px; color: #1565c0; }
  .blog-title { font-size: 15px; font-weight: 600; color: #111; margin-bottom: 0.75rem; }
  .tip { font-size: 12px; color: #999; margin-top: 0.75rem; line-height: 1.6; }
  .copy-btn {
    margin-top: 1rem;
    padding: 6px 14px;
    font-size: 12px;
    border: 1px solid #ccc;
    border-radius: 6px;
    background: #f5f5f5;
    cursor: pointer;
    color: #444;
  }
  .copy-btn:hover { background: #e8e8e8; }
  .copy-btn.copied { background: #e8f5e9; border-color: #a5d6a7; color: #2e7d32; }
</style>

<div class="wrap">

  <!-- 블로그 -->
  <div class="card">
    <div class="card-header">
      <span class="channel-label">✏️ 블로그</span>
      <span class="badge blog-badge">정보형 · 500자+</span>
      <span class="char-count">~560자</span>
    </div>
    <div class="card-body">
      <div class="blog-title">☀️ 초6 학부모님, 이번 여름이 중학 영어의 분기점입니다 — 배사메무초 영어학원 여름방학 특강 조기등록 20% 할인</div>
      <p id="blog-text">중학교 입학 후 영어 때문에 힘들어하는 아이들, 공통점이 있습니다. 초6 여름방학을 그냥 보냈다는 것.

배사메무초 영어학원의 이번 여름방학 특강은 초등 6학년을 위한 중등 영어 선행학습 반으로, 중1 교과 어휘·문법·독해를 미리 체계적으로 잡아드립니다.

📌 특강 커리큘럼
• 중1 핵심 문법 완성 (시제·문장 구조·품사)
• 중등 필수 어휘 600 집중 암기
• 지문 독해 훈련 및 서술형 대비
• 소수 정예 운영으로 밀착 관리

🎯 조기등록 혜택
7월 5일까지 등록하시면 수강료 20% 즉시 할인!
마감 후에는 정가로만 등록 가능하니 서두르세요.

중학교 첫 영어 시험, 자신 있게 시작하고 싶은 아이라면 지금이 기회입니다.
배사메무초 영어학원으로 상담 문의 주세요 📞</p>
      <button class="copy-btn" onclick="copyText('blog-text', this)">📋 복사</button>
      <div class="tip">💡 추천 키워드: '초6 중등영어 선행', '배사메무초 영어학원 여름방학 특강', '초등 영어학원 조기등록 할인'</div>
    </div>
  </div>

  <!-- 인스타그램 -->
  <div class="card">
    <div class="card-header">
      <span class="channel-label">📸 인스타그램</span>
      <span class="badge insta-badge">감성형 · 150자 이내</span>
      <span class="char-count">~128자</span>
    </div>
    <div class="card-body">
      <p id="insta-text">초6, 이 여름이 중학 영어를 결정합니다 ☀️
배사메무초 영어학원 여름방학 특강
중등 선행반 조기등록 — 7월 5일까지 20% 할인.
먼저 시작한 아이가 중1 첫 시험을 웃습니다 ✏️</p>
      <div class="tags">
        <span class="tag">#배사메무초영어학원</span>
        <span class="tag">#여름방학특강</span>
        <span class="tag">#초6영어</span>
        <span class="tag">#중등영어선행</span>
        <span class="tag">#조기등록할인</span>
        <span class="tag">#중1영어준비</span>
        <span class="tag">#초등영어학원</span>
        <span class="tag">#방학공부</span>
      </div>
      <button class="copy-btn" onclick="copyText('insta-text', this)">📋 복사</button>
      <div class="tip">💡 피드 이미지: "중1 첫 시험, 이미 준비된 아이가 있습니다" 카드뉴스 + 20% 강조 디자인 추천</div>
    </div>
  </div>

  <!-- 카카오채널 -->
  <div class="card">
    <div class="card-header">
      <span class="channel-label">💬 카카오채널</span>
      <span class="badge kakao-badge">친근형 · 180자 이내</span>
      <span class="char-count">~162자</span>
    </div>
    <div class="card-body">
      <p id="kakao-text">☀️ [여름방학 특강 조기등록 안내]

안녕하세요, 배사메무초 영어학원입니다 😊
초6 중등 영어 선행반 특강 오픈했어요!

✅ 7월 5일까지 조기등록 → 20% 할인
✅ 선착순 마감 — 자리 얼마 안 남았어요!

중1 올라가기 전 이번 여름, 딱 한 번의 기회예요 🙌
궁금하신 점은 채팅으로 편하게 물어보세요 👇</p>
      <button class="copy-btn" onclick="copyText('kakao-text', this)">📋 복사</button>
      <div class="tip">💡 발송 타이밍: 평일 오전 10~11시 또는 오후 7~8시 / 마감 3일 전 리마인드 1회 추가 권장</div>
    </div>
  </div>

</div>

<script>
function copyText(id, btn) {
  const text = document.getElementById(id).innerText;
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = '✅ 복사됨!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = '📋 복사';
      btn.classList.remove('copied');
    }, 2000);
  });
}
</script>
"""

components.html(html_content, height=1500, scrolling=True)
