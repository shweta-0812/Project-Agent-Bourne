import gql from 'graphql-tag'

const SAMPLE_USER_DETAIL = gql`
    query SampleUserDetail {
        sampleUserDetail {
            id
            email
            name
        }
    }
`;

export {
    SAMPLE_USER_DETAIL
};