import gql from 'graphql-tag'

export const RUN_TASK_MUTATION = gql`
    mutation RunTask {
        runTask(taskId: 1, taskPrompt: "File PIL in Supreme Court of India for stopping cutting down of trees in Nicobar Islands") {
            runTaskObj {
                taskId
            },
            taskResult,
            ok
        }
    }
`;