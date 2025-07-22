# 🧠 Blind75 Offline Practice Template

Hi! I’m **Shubhada** 👋

I built this template so I could **practice LeetCode’s Blind 75 problems while traveling**, especially on long flights without Wi-Fi. After realizing it might help others too, I cleaned it up and made it easy to use **completely offline**.

Whether you’re prepping for interviews, brushing up on core patterns, or just looking for an organized way to work through Blind 75, I hope this repo keeps you consistent and focused — even without internet access. ✈️💻

---

## 📦 What’s Included

| ✅ | Item |
|----|------|
| **Pre-created files** for every Blind 75 problem |
| **Topic folders** for structured practice (Arrays, Trees, Sliding Window, …) |
| **`blind75_questions.pdf`** — all prompts offline |
| **NeetCode resources** (`ResourcesFromNeetcode/`): full Python solutions & hints |
| Lightweight starter stubs so you can code & run tests locally |

---

## 🗂 Folder Structure

```
Blind75Prep/
├── Arrays&Hashing/
│   ├── TwoSum.py
│   ├── ...
├── SlidingWindow/
├── Trees/
├── ...
├── ResourcesFromNeetcode/
│   ├── neetcode-hints/
│   └── neetcode-python-solutions/
├── blind75_questions.pdf
└── README.md
```

---

## ⚙️ How to Use

### 1️⃣  Write Your Solution  
Each file has a stub you can fill in:

```python
# Arrays&Hashing/TwoSum.py
def twoSum(nums, target):
    # ✍️  your code here
    pass
```

---

### 2️⃣  Test Your Solution (manual for now)  

> An automatic test runner is planned.  
> For now, add a quick check function:

```python
def check(fn, args, expected):
    out = fn(*args)
    print("✅ PASS" if out == expected else f"❌ FAIL  – got {out}, expected {expected}")

if __name__ == "__main__":
    check(twoSum, ([2, 7, 11, 15], 9), [0, 1])
```

---

### 3️⃣  Run the File

```bash
python Arrays&Hashing/TwoSum.py
```

Make sure your VS Code interpreter is set to Python.

---

### 4️⃣  Compare with NeetCode

After solving, open the matching reference in  
`ResourcesFromNeetcode/neetcode-python-solutions/` to:

- Compare logic & structure  
- Spot optimizations  
- Learn Pythonic patterns  

---

## 💡  Tips

- Keep notes or edge-case gotchas in comments right inside the file.  
- When you’re ready, add `pytest` or your favorite framework for faster feedback.  
- Feel free to fork & tweak the folder names or add your own problems.

---

## 📚  Credits

- Problem statements adapted from **LeetCode**  
- Solutions & hints sourced from the awesome [**NeetCode repo**](https://github.com/neetcode-gh/leetcode)

---

*Happy coding & good luck on your interview prep!* 🚀
