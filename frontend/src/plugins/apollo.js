import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client/core';
import { provideApolloClient } from '@vue/apollo-composable';

const httpLink = createHttpLink({
    // uri: 'http://127.0.0.1:8000/graphql'
    uri: import.meta.env.VITE_APOLLO_URL,
    // headers: {'X-CSRFToken': ''} // need to check cookie and set manually
});

const cache = new InMemoryCache();

const apolloClient = new ApolloClient({
    link: httpLink,
    cache,
});

export function useApollo() {
    provideApolloClient(apolloClient)
};

export default apolloClient;

