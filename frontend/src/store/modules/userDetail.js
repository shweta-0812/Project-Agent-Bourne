import { defineStore } from 'pinia';

export const userDetail = defineStore('userDetail', {
    state: () => ({
        user_id: null,
        name: null,
        email: null,
        picture: null,
        isAdmin: false,
    }),
    actions: {
        // async registerUser(login, password)  {
        //     const csrfToken = getCookie('csrftoken');
        //     const response = await fetch('http://localhost:8000/register-user', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json',
        //             'X-CSRFToken': csrfToken,
        //         },
        //         body: JSON.stringify({}),
        //     });
        //     // Check if the response is OK
        //     if (response.ok) {}
        //     },
    },
    getters: {
        isAuthenticatedUser (state) {
            let isAuthenticated = false;
            const JWT = localStorage.getItem('JwtToken');

            if((JWT !== 'undefined' || JWT !== '' || JWT !== null) &&
                (state.name !=='' || state !== undefined)){
                isAuthenticated = true;
            }
            return isAuthenticated;
        },

        getUser(state) {
            let user = {}
            user['user_id'] = state.user_id
            user['name'] = state.name
            user['email'] = state.email
            user['picture'] = state.picture
            user['isAdmin'] = state.isAdmin
            user['isAuthenticated'] = state.isAuthenticatedUser()

            return user;
        }
    },
    persist: {
        storage: sessionStorage, // data in sessionStorage is cleared when the page session ends.
    },
});