import gql from 'graphql-tag'

const GET_USERS_LIST = gql`
    query GetUsersList {
        userDetails {
            id
            email
            name,
            isAdmin,
            userType,
            clientId,
            profilePicUrl
        }
    }
`;

export {
    GET_USERS_LIST
};