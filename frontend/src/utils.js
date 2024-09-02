export function generateSecureRandomString(length) {
    const array = new Uint8Array(length);
    window.crypto.getRandomValues(array);
    return Array.from(array, byte => ('0' + byte.toString(16)).slice(-2)).join('').slice(0, length);
}

export function setInLocalStorage(key, value) {
    localStorage.setItem(key,value);
}

export function getFromLocalStorage(key) {
    return localStorage.getItem(key)
}

export function getCookie(cookieName) {
    let cookieValue = '';
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, cookieName.length + 1) === (cookieName + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(cookieName.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}