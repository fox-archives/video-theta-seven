#!/usr/bin/env -S deno run --allow-write --allow-read ./scripts/ticker-convert.js

const companyTickers = JSON.parse(await Deno.readTextFile('./data/company_tickers.json'))

const entries = []
for (const [_property, object] of Object.entries(companyTickers)) {
    entries.push(object)
}

await Deno.writeTextFile('./data/company_tickers_pretty.json', JSON.stringify({ entries }, null, '\t'))
