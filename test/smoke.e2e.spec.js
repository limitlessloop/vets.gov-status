module.exports = {
    'Smoke Test': client => {
        const date = new Date();
        const displayDate = date.toLocaleString('default', { month: 'long' }) + ' ' + date.getDate()+ ', ' + date.getFullYear();

        client
            // .url('http://localhost:4000/scorecard/')
            .url(' https://dev.va.gov/scorecard/')
            .waitForElementVisible('body', 2000)
            .assert.title('VA.gov Performance');

        client.click("#chart-nav-users");
        client.expect.element("#usersChart").to.be.visible;
        client.expect.element("#transactionsChart").not.to.be.visible;

        client.click("#chart-nav-transactions");
        client.expect.element("#transactionsChart").to.be.visible;
        client.expect.element("#usersChart").not.to.be.visible;

        //Verify keyboard navigability, press TAB to reach the intended element
        client.keys(client.Keys.TAB);
        client.keys(client.Keys.TAB);
        client.keys(client.Keys.TAB);

        // client.expect.element("#accordion-apply-for-disability-benefits").to.be.visible;
        // client.keys(client.Keys.ENTER);
        // client.expect.element("#accordion-apply-for-disability-benefits").to.not.be.visible;

        client.expect.element("#last-updated-date").text.to.equal(displayDate);
    }
};
