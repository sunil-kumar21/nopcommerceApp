pytest -s -v -m "sanity" --html=./Reports/report.html testcases/  --browser  chrome
pytest -s -v -m "sanity" --html=./Reports/report.html testcases/  --browser  firefox

rem pytest -s -v -m "sanity or regressoin" --html=./Reports/report.html testcases/  --browser chrome
rem pytest -s -v -m "sanity and regressoin" --html=./Reports/report.html testcases/  --browser chrome
rem pytest -s -v -m "regressoin" --html=./Reports/report.html testcases/  --browser chrome

