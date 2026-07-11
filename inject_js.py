with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')

target = """    if (window.Babel && typeof window.Babel.transformScriptTags === "function") {
      window.Babel.transformScriptTags();
    }"""

# In case the double quotes or spacing are slightly different in index.html, let's find a looser target
target_loose = "window.Babel.transformScriptTags();"
idx = content.find(target_loose)

if idx != -1:
    # Insert right after the if statement block
    insert_pos = content.find('}', idx) + 1
    
    js_code = """
    
    // ════ 주보 이미지 뷰어 스크립트 ════
    (function() {
      var images = [
        'smallpdf-convert-20260628-072758/0.jpg',
        'smallpdf-convert-20260628-072758/1.jpg',
        'smallpdf-convert-20260628-072758/2.jpg',
        'smallpdf-convert-20260628-072758/3.jpg',
        'smallpdf-convert-20260628-072758/4.jpg',
        'smallpdf-convert-20260628-072758/5.jpg',
        'smallpdf-convert-20260628-072758/6.jpg',
        'smallpdf-convert-20260628-072758/7.jpg',
        'smallpdf-convert-20260628-072758/8.jpg',
        'smallpdf-convert-20260628-072758/9.jpg',
        'smallpdf-convert-20260628-072758/10.jpg',
        'smallpdf-convert-20260628-072758/11.jpg',
        'smallpdf-convert-20260628-072758/12.jpg',
        'smallpdf-convert-20260628-072758/13.jpg'
      ];
      var currentIndex = 0;
      
      function getViewerElements() {
        return {
          modal: document.getElementById('bulletin-viewer-modal'),
          img: document.getElementById('viewer-img'),
          indicator: document.getElementById('viewer-page-indicator'),
          btnView: document.getElementById('btn-view-bulletin'),
          btnClose: document.getElementById('modal-close-btn'),
          btnPrev: document.getElementById('viewer-prev-btn'),
          btnNext: document.getElementById('viewer-next-btn')
        };
      }
      
      function showImage(els, idx) {
        if (idx < 0) idx = images.length - 1;
        if (idx >= images.length) idx = 0;
        currentIndex = idx;
        if (els.img) els.img.src = images[currentIndex];
        if (els.indicator) els.indicator.textContent = (currentIndex + 1) + ' / ' + images.length;
      }
      
      document.addEventListener('click', function(e) {
        var els = getViewerElements();
        
        // 1. Click view button
        if (e.target && (e.target.id === 'btn-view-bulletin' || e.target.closest('#btn-view-bulletin'))) {
          if (els.modal) {
            els.modal.style.display = 'flex';
            setTimeout(function() {
              els.modal.classList.add('active');
            }, 10);
            showImage(els, 0);
          }
        }
        
        // 2. Click close button
        if (e.target && e.target.id === 'modal-close-btn') {
          if (els.modal) {
            els.modal.classList.remove('active');
            setTimeout(function() {
              els.modal.style.display = 'none';
            }, 300);
          }
        }
        
        // 3. Click backdrop
        if (e.target && e.target.id === 'bulletin-viewer-modal') {
          if (els.modal) {
            els.modal.classList.remove('active');
            setTimeout(function() {
              els.modal.style.display = 'none';
            }, 300);
          }
        }
        
        // 4. Click prev button
        if (e.target && e.target.id === 'viewer-prev-btn') {
          showImage(els, currentIndex - 1);
        }
        
        // 5. Click next button
        if (e.target && e.target.id === 'viewer-next-btn') {
          showImage(els, currentIndex + 1);
        }
      });
      
      document.addEventListener('keydown', function(e) {
        var els = getViewerElements();
        if (!els.modal || !els.modal.classList.contains('active')) return;
        
        if (e.key === 'ArrowLeft') {
          showImage(els, currentIndex - 1);
        } else if (e.key === 'ArrowRight') {
          showImage(els, currentIndex + 1);
        } else if (e.key === 'Escape') {
          els.modal.classList.remove('active');
          setTimeout(function() { els.modal.style.display = 'none'; }, 300);
        }
      });
    })();"""
    
    content = content[:insert_pos] + js_code + content[insert_pos:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Javascript viewer controller injected into index.html successfully.")
else:
    print("Error: Could not find Babel.transformScriptTags in index.html.")
