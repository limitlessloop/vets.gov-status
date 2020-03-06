module.exports = {
    'Smoke Test': client => {
        client
            .url('http://localhost:4000/scorecard/')
            .waitForElementVisible('body', 2000)
            .assert.title('Scorecard')
    }
}