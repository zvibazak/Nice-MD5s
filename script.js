document.addEventListener('DOMContentLoaded', () => {
    let counter = 0;
    let workers = [];
    let currentRecord = 12;
    let nValue = currentRecord + 1;

    const nValueDisplay = document.getElementById('nValueDisplay');
    const counterDisplay = document.getElementById('counter');
    const workersCountDisplay = document.getElementById('workersCount');
    const recordDisplay = document.getElementById('record');

    nValueDisplay.innerText = nValue;

    document.getElementById('increaseN').addEventListener('click', () => {
        nValue++;
        nValueDisplay.innerText = nValue;
    });

    document.getElementById('decreaseN').addEventListener('click', () => {
        if (nValue > 1) {
            nValue--;
            nValueDisplay.innerText = nValue;
        }
    });

    document.getElementById('startButton').addEventListener('click', startCalculation);
    document.getElementById('stopButton').addEventListener('click', stopCalculation);

    function startCalculation() {
        if (workers.length > 0) return; // Prevent starting multiple workers
        for (let i = 0; i < navigator.hardwareConcurrency; i++) {
            const blob = new Blob([getWorkerScript()], { type: 'application/javascript' });
            const worker = new Worker(URL.createObjectURL(blob));

            worker.onmessage = (e) => {
                if (e.data.type === 'increment') {
                    counter += e.data.count; // Increment in bulk for better performance
                    counterDisplay.innerText = counter.toLocaleString();
                } else if (e.data.type === 'newRecord') {
                    currentRecord = e.data.length;
                    recordDisplay.innerText = `N = ${currentRecord}`;
                    alert(`New match found! N = ${currentRecord}, Input: ${e.data.string}, MD5 Hash: ${e.data.hash}. Please submit a pull request with N = ${currentRecord} on the GitHub page.`);
                    stopCalculation();
                }
            };
            workers.push(worker);
        }
        updateWorkersCount();
    }

    function stopCalculation() {
        workers.forEach(worker => worker.terminate());
        workers = [];
        updateWorkersCount();
    }

    function updateWorkersCount() {
        workersCountDisplay.innerText = workers.length;
    }

    function getWorkerScript() {
        return `
            self.importScripts('https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/crypto-js.js');

            const targetN = ${nValue};

            function generateRandomString(length = 32) {
                const characters = 'abcdef0123456789';
                let result = '';
                for (let i = 0; i < length; i++) {
                    result += characters.charAt(Math.floor(Math.random() * characters.length));
                }
                return result;
            }

            function md5(inputString) {
                return CryptoJS.MD5(inputString).toString();
            }

            function calculate() {
                function runBatch() {
                    let localCounter = 0;
                    for (let j = 0; j < 1000; j++) { // Increased batch size for performance
                        const x = generateRandomString();
                        const md5Value = md5(x);
                        localCounter++;
                        let matchingChars = 0;
                        while (matchingChars < x.length && x[matchingChars] === md5Value[matchingChars]) {
                            matchingChars++;
                        }
                        if (matchingChars >= targetN) {
                            postMessage({ type: 'newRecord', length: matchingChars, string: x, hash: md5Value });
                            return; // Stop calculation once we find the first result
                        }
                    }
                    postMessage({ type: 'increment', count: localCounter });
                    setTimeout(runBatch, 0); // Use setTimeout for yielding to keep UI responsive
                }
                runBatch();
            }

            calculate();
        `;
    }
});

