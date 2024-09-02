import { defineStore } from 'pinia';

export const counter = defineStore('counter', {
    state: () => ({
        count: 0
    }),
    actions: {
        increment() {
            this.count++
        }
    }
});