module.exports = {
    'Smoke Test': client => {
        client
            .url('http://localhost:4000/scorecard/')
            .waitForElementVisible('body', 2000)

            .assert.title('Scorecard')

            client.expect.element("ul.nav.nav-tabs.tabs-chart > li:nth-child(1)").text.to.equal("Users")
            client.expect.element("ul.nav.nav-tabs.tabs-chart > li:nth-child(2)").text.to.equal("Mobile Use")
            client.expect.element("ul.nav.nav-tabs.tabs-chart > li:nth-child(3)").text.to.equal("Views")
            client.expect.element("ul.nav.nav-tabs.tabs-chart > li:nth-child(4)").text.to.equal("New accounts")
            client.expect.element("ul.nav.nav-tabs.tabs-chart > li:nth-child(5)").text.to.equal("Total accounts")


            client.expect.element('a[href="/scorecard/boards/content.html"]').to.be.present
            client.expect.element('a[href="/scorecard/boards/discharge.html"]').to.be.present
            client.expect.element('a[href="/scorecard/boards/facility.html"]').to.be.present
            client.expect.element('a[href="/scorecard/boards/gibct.html"]').to.be.present
            client.expect.element('a[href="/scorecard/boards/search.html"]').to.be.present



    }
}