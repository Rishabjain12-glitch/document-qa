<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Q&A - Ask Questions About Your Files</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #ffffff;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
        }
        
        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }
        
        .brand {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px 40px;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        
        .brand-name {
            font-size: 2em;
            font-weight: 700;
            margin: 0;
            color: #fff;
        }
        
        .brand-tagline {
            font-size: 0.9em;
            color: rgba(255, 255, 255, 0.9);
            margin-top: 5px;
        }
        
        h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
        }
        
        .icon {
            font-size: 2em;
        }
        
        .subtitle {
            font-size: 1.1em;
            opacity: 0.95;
        }
        
        .main-card {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            padding: 40px;
            margin-bottom: 20px;
            border: 2px solid transparent;
            background-clip: padding-box;
            position: relative;
            overflow: hidden;
        }
        
        .main-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            border-radius: 20px;
            padding: 2px;
            z-index: -1;
        }
        
        .main-card::after {
            content: '';
            position: absolute;
            top: 2px;
            left: 2px;
            right: 2px;
            bottom: 2px;
            background: white;
            border-radius: 18px;
            z-index: -1;
        }
        
        .section {
            margin-bottom: 30px;
        }
        
        .section-title {
            font-size: 1.3em;
            color: #333;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        label {
            display: block;
            font-size: 0.95em;
            color: #555;
            margin-bottom: 8px;
            font-weight: 500;
        }
        
        input[type="password"],
        textarea,
        input[type="file"] {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-family: inherit;
            font-size: 1em;
            transition: all 0.3s ease;
        }
        
        input[type="password"]:focus,
        textarea:focus,
        input[type="file"]:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        textarea {
            resize: vertical;
            min-height: 120px;
        }
        
        .file-upload-wrapper {
            position: relative;
        }
        
        input[type="file"] {
            cursor: pointer;
            background: #f8f9fa;
        }
        
        .file-name {
            margin-top: 10px;
            padding: 12px 15px;
            background: #e8f5e9;
            border-radius: 8px;
            color: #2e7d32;
            font-size: 0.95em;
            display: none;
        }
        
        .file-name.show {
            display: block;
        }
        
        .button-group {
            display: flex;
            gap: 12px;
            margin-top: 25px;
        }
        
        button {
            flex: 1;
            padding: 14px 24px;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        
        .btn-primary:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        
        .btn-primary:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .btn-secondary {
            background: #f0f0f0;
            color: #333;
            border: 2px solid #e0e0e0;
        }
        
        .btn-secondary:hover {
            background: #e8e8e8;
        }
        
        .info-box {
            padding: 15px 20px;
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            border-radius: 6px;
            color: #1565c0;
            margin-bottom: 20px;
            display: none;
        }
        
        .info-box.show {
            display: block;
        }
        
        .info-box a {
            color: #1565c0;
            text-decoration: none;
            font-weight: 600;
        }
        
        .info-box a:hover {
            text-decoration: underline;
        }
        
        .response-section {
            margin-top: 30px;
            padding-top: 30px;
            border-top: 2px solid #e0e0e0;
        }
        
        .response-box {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            line-height: 1.6;
            color: #333;
            display: none;
        }
        
        .response-box.show {
            display: block;
        }
        
        .loading {
            display: flex;
            align-items: center;
            gap: 10px;
            color: #667eea;
            margin: 20px 0;
            display: none;
        }
        
        .loading.show {
            display: flex;
        }
        
        .spinner {
            border: 3px solid #e0e0e0;
            border-top: 3px solid #667eea;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .error {
            padding: 15px 20px;
            background: #ffebee;
            border-left: 4px solid #f44336;
            border-radius: 6px;
            color: #c62828;
            margin: 15px 0;
            display: none;
        }
        
        .error.show {
            display: block;
        }
        
        .trust-badge {
            background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 25px 0;
            text-align: center;
            border: 2px solid #0d47a1;
        }
        
        .trust-badge h3 {
            margin: 0 0 12px 0;
            font-size: 1.2em;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        
        .trust-features {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 15px;
            font-size: 0.95em;
        }
        
        .trust-feature {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .trust-feature-icon {
            font-size: 1.3em;
        }
        
        @media (max-width: 600px) {
            .trust-features {
                grid-template-columns: 1fr;
            }
        }
        
        .success {
            padding: 15px 20px;
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            border-radius: 6px;
            color: #2e7d32;
            margin: 15px 0;
            display: none;
        }
        
        .success.show {
            display: block;
        }
        
        @media (max-width: 600px) {
            h1 {
                font-size: 1.8em;
            }
            
            .main-card {
                padding: 25px;
            }
            
            .button-group {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="brand">
                <p class="brand-name">✨ Magic Bus</p>
                <p class="brand-tagline">Secure Document Intelligence</p>
            </div>
            <h1>
                <span class="icon">📄</span>
                Document Q&A
            </h1>
            <p class="subtitle">Upload a document and ask questions – powered by AI</p>
        </header>
        
        <div class="main-card">
            <!-- Trust & Security Badge -->
            <div class="trust-badge">
                <h3>
                    <span>🔒</span>
                    Trusted & Secure
                </h3>
                <div class="trust-features">
                    <div class="trust-feature">
                        <span class="trust-feature-icon">🛡️</span>
                        <span>End-to-End Encrypted</span>
                    </div>
                    <div class="trust-feature">
                        <span class="trust-feature-icon">🚫</span>
                        <span>Zero Data Storage</span>
                    </div>
                    <div class="trust-feature">
                        <span class="trust-feature-icon">👁️</span>
                        <span>No Data Tracking</span>
                    </div>
                    <div class="trust-feature">
                        <span class="trust-feature-icon">✅</span>
                        <span>Privacy Guaranteed</span>
                    </div>
                </div>
                <p style="margin: 15px 0 0 0; font-size: 0.9em; opacity: 0.95;">
                    Your documents are never stored on our servers. Data is processed instantly and permanently deleted.
                </p>
            </div>
            <!-- API Key Section -->
            <div class="section">
                <label for="apiKey">🔑 OpenAI API Key</label>
                <input 
                    type="password" 
                    id="apiKey" 
                    placeholder="sk-..." 
                    autocomplete="off"
                >
                <p style="font-size: 0.85em; color: #999; margin-top: 8px;">
                    Get your free API key at <a href="https://platform.openai.com/account/api-keys" target="_blank" style="color: #667eea; text-decoration: none;">OpenAI Platform</a>
                </p>
            </div>
            
            <!-- Info Box -->
            <div class="info-box" id="infoBox">
                🗝️ Please add your OpenAI API key to continue.
            </div>
            
            <!-- File Upload Section -->
            <div class="section">
                <label for="fileInput">📁 Upload Document</label>
                <div class="file-upload-wrapper">
                    <input 
                        type="file" 
                        id="fileInput" 
                        accept=".txt,.md" 
                        disabled
                    >
                    <div class="file-name" id="fileName"></div>
                </div>
            </div>
            
            <!-- Question Section -->
            <div class="section">
                <label for="question">❓ Ask a Question</label>
                <textarea 
                    id="question" 
                    placeholder="Can you give me a short summary?" 
                    disabled
                ></textarea>
            </div>
            
            <!-- Buttons -->
            <div class="button-group">
                <button class="btn-primary" id="submitBtn" disabled>
                    Get Answer
                </button>
                <button class="btn-secondary" id="clearBtn">
                    Clear All
                </button>
            </div>
            
            <!-- Error/Success Messages -->
            <div class="error" id="errorMsg"></div>
            <div class="success" id="successMsg"></div>
            
            <!-- Loading Indicator -->
            <div class="loading" id="loading">
                <div class="spinner"></div>
                <span>Getting answer from AI...</span>
            </div>
            
            <!-- Response Section -->
            <div class="response-section" id="responseSection" style="display: none;">
                <h3 style="color: #333; margin-bottom: 15px;">📝 Answer</h3>
                <div class="response-box" id="responseBox"></div>
            </div>
        </div>
    </div>
    
    <script>
        const apiKeyInput = document.getElementById('apiKey');
        const fileInput = document.getElementById('fileInput');
        const questionInput = document.getElementById('question');
        const submitBtn = document.getElementById('submitBtn');
        const clearBtn = document.getElementById('clearBtn');
        const infoBox = document.getElementById('infoBox');
        const fileName = document.getElementById('fileName');
        const loading = document.getElementById('loading');
        const responseBox = document.getElementById('responseBox');
        const responseSection = document.getElementById('responseSection');
        const errorMsg = document.getElementById('errorMsg');
        const successMsg = document.getElementById('successMsg');
        
        let currentFile = null;
        
        // Handle API Key Input
        apiKeyInput.addEventListener('input', () => {
            const hasKey = apiKeyInput.value.trim().length > 0;
            fileInput.disabled = !hasKey;
            questionInput.disabled = !hasKey;
            infoBox.classList.toggle('show', !hasKey);
            updateSubmitBtn();
        });
        
        // Handle File Upload
        fileInput.addEventListener('change', (e) => {
            currentFile = e.target.files[0];
            if (currentFile) {
                fileName.textContent = `✓ ${currentFile.name}`;
                fileName.classList.add('show');
                successMsg.textContent = `File loaded: ${currentFile.name}`;
                successMsg.classList.add('show');
            } else {
                fileName.classList.remove('show');
            }
            updateSubmitBtn();
        });
        
        // Handle Question Input
        questionInput.addEventListener('input', updateSubmitBtn);
        
        // Update Submit Button State
        function updateSubmitBtn() {
            const hasKey = apiKeyInput.value.trim().length > 0;
            const hasFile = currentFile !== null;
            const hasQuestion = questionInput.value.trim().length > 0;
            submitBtn.disabled = !(hasKey && hasFile && hasQuestion);
        }
        
        // Clear All
        clearBtn.addEventListener('click', () => {
            apiKeyInput.value = '';
            fileInput.value = '';
            questionInput.value = '';
            currentFile = null;
            fileName.classList.remove('show');
            responseSection.style.display = 'none';
            errorMsg.classList.remove('show');
            successMsg.classList.remove('show');
            fileInput.disabled = true;
            questionInput.disabled = true;
            updateSubmitBtn();
        });
        
        // Submit Question
        submitBtn.addEventListener('click', async () => {
            if (!currentFile || !questionInput.value.trim()) return;
            
            try {
                errorMsg.classList.remove('show');
                successMsg.classList.remove('show');
                loading.classList.add('show');
                
                // Read file
                const fileContent = await currentFile.text();
                
                // Call OpenAI API
                const response = await fetch('https://api.openai.com/v1/chat/completions', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${apiKeyInput.value}`
                    },
                    body: JSON.stringify({
                        model: 'gpt-3.5-turbo',
                        messages: [
                            {
                                role: 'user',
                                content: `Here's a document:\n\n${fileContent}\n\n---\n\nQuestion: ${questionInput.value}`
                            }
                        ],
                        temperature: 0.7,
                        max_tokens: 2000
                    })
                });
                
                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.error?.message || 'API Error');
                }
                
                const data = await response.json();
                const answer = data.choices[0].message.content;
                
                // Display response
                responseBox.textContent = answer;
                responseBox.classList.add('show');
                responseSection.style.display = 'block';
                loading.classList.remove('show');
                
            } catch (error) {
                loading.classList.remove('show');
                errorMsg.textContent = `❌ Error: ${error.message}`;
                errorMsg.classList.add('show');
            }
        });
        
        // Initial state
        updateSubmitBtn();
    </script>
</body>
</html>
