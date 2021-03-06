# -*- coding: utf-8 -*-
# WARNING: Autogenerated code. Do not edit manually.
from mcrpc.responses import *


class BaseApiMethods:

    def getbestblockhash(self):
        return self._call("getbestblockhash")

    def getblock(self, hash_or_height, verbose=None):
        return self._call("getblock", hash_or_height, verbose)

    def getblockchaininfo(self):
        data = self._call("getblockchaininfo")
        return Getblockchaininfo(**data)

    def getblockcount(self):
        return self._call("getblockcount")

    def getblockhash(self, index):
        return self._call("getblockhash", index)

    def getchaintips(self):
        return self._call("getchaintips")

    def getdifficulty(self):
        return self._call("getdifficulty")

    def getmempoolinfo(self):
        data = self._call("getmempoolinfo")
        return Getmempoolinfo(**data)

    def getrawmempool(self, verbose=None):
        return self._call("getrawmempool", verbose)

    def gettxout(self, txid, n, includemempool=None):
        return self._call("gettxout", txid, n, includemempool)

    def gettxoutsetinfo(self):
        data = self._call("gettxoutsetinfo")
        return Gettxoutsetinfo(**data)

    def listassets(self, asset_identifiers=None, verbose=None, count=None, start=None):
        return self._call("listassets", asset_identifiers, verbose, count, start)

    def listblocks(self, block_set_identifier, verbose=None):
        return self._call("listblocks", block_set_identifier, verbose)

    def listpermissions(self, permissions=None, addresses=None, verbose=None):
        return self._call("listpermissions", permissions, addresses, verbose)

    def liststreams(self, stream_identifiers=None, verbose=None, count=None, start=None):
        return self._call("liststreams", stream_identifiers, verbose, count, start)

    def listupgrades(self, upgrade_identifiers=None):
        return self._call("listupgrades", upgrade_identifiers)

    def verifychain(self, checklevel=None, numblocks=None):
        return self._call("verifychain", checklevel, numblocks)

    def clearmempool(self):
        return self._call("clearmempool")

    def getblockchainparams(self, displaynames=None, with_upgrades=None):
        return self._call("getblockchainparams", displaynames, with_upgrades)

    def getinfo(self):
        data = self._call("getinfo")
        return Getinfo(**data)

    def getruntimeparams(self):
        data = self._call("getruntimeparams")
        return Getruntimeparams(**data)

    def help(self, command=None):
        return self._call("help", command)

    def pause(self, tasks):
        return self._call("pause", tasks)

    def resume(self, tasks):
        return self._call("resume", tasks)

    def setlastblock(self, hash_or_height=None):
        return self._call("setlastblock", hash_or_height)

    def setruntimeparam(self, parameter_name, parameter_value):
        return self._call("setruntimeparam", parameter_name, parameter_value)

    def stop(self):
        return self._call("stop")

    def getgenerate(self):
        return self._call("getgenerate")

    def gethashespersec(self):
        return self._call("gethashespersec")

    def setgenerate(self, generate, genproclimit=None):
        return self._call("setgenerate", generate, genproclimit)

    def getblocktemplate(self, jsonrequestobject=None):
        return self._call("getblocktemplate", jsonrequestobject)

    def getmininginfo(self):
        data = self._call("getmininginfo")
        return Getmininginfo(**data)

    def getnetworkhashps(self, blocks=None, height=None):
        return self._call("getnetworkhashps", blocks, height)

    def prioritisetransaction(self, txid, priority_delta, fee_delta):
        return self._call("prioritisetransaction", txid, priority_delta, fee_delta)

    def submitblock(self, hexdata, jsonparametersobject=None):
        return self._call("submitblock", hexdata, jsonparametersobject)

    def addnode(self, node, add_or_remove_or_onetry):
        return self._call("addnode", node, add_or_remove_or_onetry)

    def getaddednodeinfo(self, dns, node=None):
        return self._call("getaddednodeinfo", dns, node)

    def getconnectioncount(self):
        return self._call("getconnectioncount")

    def getnettotals(self):
        data = self._call("getnettotals")
        return Getnettotals(**data)

    def getnetworkinfo(self):
        data = self._call("getnetworkinfo")
        return Getnetworkinfo(**data)

    def getpeerinfo(self):
        return self._call("getpeerinfo")

    def ping(self):
        return self._call("ping")

    def appendrawchange(self, tx_hex_address, native_fee=None):
        return self._call("appendrawchange", tx_hex_address, native_fee)

    def appendrawdata(self, tx_hex_data):
        return self._call("appendrawdata", tx_hex_data)

    def decoderawtransaction(self, tx_hex):
        return self._call("decoderawtransaction", tx_hex)

    def decodescript(self, script_hex):
        return self._call("decodescript", script_hex)

    def getrawtransaction(self, txid, verbose=None):
        return self._call("getrawtransaction", txid, verbose)

    def sendrawtransaction(self, tx_hex_, allowhighfees=None):
        return self._call("sendrawtransaction", tx_hex_, allowhighfees)

    def createkeypairs(self, count=None):
        return self._call("createkeypairs", count)

    def createmultisig(self, nrequired, keys):
        return self._call("createmultisig", nrequired, keys)

    def estimatefee(self, nblocks):
        return self._call("estimatefee", nblocks)

    def estimatepriority(self, nblocks):
        return self._call("estimatepriority", nblocks)

    def validateaddress(self, address_or_pubkey_or_privkey):
        return self._call("validateaddress", address_or_pubkey_or_privkey)

    def verifymessage(self, address, signature, message):
        return self._call("verifymessage", address, signature, message)

    def addmultisigaddress(self, nrequired, keys, account=None):
        return self._call("addmultisigaddress", nrequired, keys, account)

    def appendrawexchange(self, hex, txid, vout, ask_assets):
        return self._call("appendrawexchange", hex, txid, vout, ask_assets)

    def approvefrom(self, from_address, upgrade_identifier, approve=None):
        return self._call("approvefrom", from_address, upgrade_identifier, approve)

    def backupwallet(self, destination):
        return self._call("backupwallet", destination)

    def combineunspent(self, addresses=None, minconf=None, maxcombines=None, mininputs=None, maxinputs=None, maxtime=None):
        return self._call("combineunspent", addresses, minconf, maxcombines, mininputs, maxinputs, maxtime)

    def completerawexchange(self, hex, txid, vout, ask_assets, data_or_publish_new_stream_item=None):
        return self._call("completerawexchange", hex, txid, vout, ask_assets, data_or_publish_new_stream_item)

    def create(self, entity_type, entity_name, open_, custom_fields=None):
        return self._call("create", entity_type, entity_name, open_, custom_fields)

    def createfrom(self, from_address, entity_type, entity_name, open_, custom_fields=None):
        return self._call("createfrom", from_address, entity_type, entity_name, open_, custom_fields)

    def createrawexchange(self, txid, vout, ask_assets):
        return self._call("createrawexchange", txid, vout, ask_assets)

    def decoderawexchange(self, tx_hex_, verbose=None):
        return self._call("decoderawexchange", tx_hex_, verbose)

    def disablerawtransaction(self, tx_hex):
        return self._call("disablerawtransaction", tx_hex)

    def dumpprivkey(self, address):
        return self._call("dumpprivkey", address)

    def dumpwallet(self, filename):
        return self._call("dumpwallet", filename)

    def encryptwallet(self, passphrase):
        return self._call("encryptwallet", passphrase)

    def getaccount(self, address):
        return self._call("getaccount", address)

    def getaccountaddress(self, account):
        return self._call("getaccountaddress", account)

    def getaddressbalances(self, address, minconf=None, includeLocked=None):
        return self._call("getaddressbalances", address, minconf, includeLocked)

    def getaddresses(self, verbose=None):
        return self._call("getaddresses", verbose)

    def getaddressesbyaccount(self, account):
        return self._call("getaddressesbyaccount", account)

    def getaddresstransaction(self, address, txid, verbose=None):
        return self._call("getaddresstransaction", address, txid, verbose)

    def getassetbalances(self, account=None, minconf=None, includeWatchonly=None, includeLocked=None):
        return self._call("getassetbalances", account, minconf, includeWatchonly, includeLocked)

    def getassettransaction(self, asset_identifier, txid, verbose=None):
        return self._call("getassettransaction", asset_identifier, txid, verbose)

    def getbalance(self, account=None, minconf=None, includeWatchonly=None):
        return self._call("getbalance", account, minconf, includeWatchonly)

    def getmultibalances(self, addresses=None, assets=None, minconf=None, includeLocked=None, includeWatchonly=None):
        return self._call("getmultibalances", addresses, assets, minconf, includeLocked, includeWatchonly)

    def getnewaddress(self, account=None):
        return self._call("getnewaddress", account)

    def getrawchangeaddress(self):
        return self._call("getrawchangeaddress")

    def getreceivedbyaccount(self, account, minconf=None):
        return self._call("getreceivedbyaccount", account, minconf)

    def getreceivedbyaddress(self, address, minconf=None):
        return self._call("getreceivedbyaddress", address, minconf)

    def getstreamitem(self, stream_identifier, txid, verbose=None):
        return self._call("getstreamitem", stream_identifier, txid, verbose)

    def getstreamkeysummary(self, stream_identifier, key, mode):
        return self._call("getstreamkeysummary", stream_identifier, key, mode)

    def getstreampublishersummary(self, stream_identifier, address, mode):
        return self._call("getstreampublishersummary", stream_identifier, address, mode)

    def gettotalbalances(self, minconf=None, includeWatchonly=None, includeLocked=None):
        return self._call("gettotalbalances", minconf, includeWatchonly, includeLocked)

    def gettransaction(self, txid, includeWatchonly=None):
        return self._call("gettransaction", txid, includeWatchonly)

    def gettxoutdata(self, txid, vout, count_bytes=None, start_byte=None):
        return self._call("gettxoutdata", txid, vout, count_bytes, start_byte)

    def getunconfirmedbalance(self):
        return self._call("getunconfirmedbalance")

    def getwalletinfo(self):
        data = self._call("getwalletinfo")
        return Getwalletinfo(**data)

    def getwallettransaction(self, txid, includeWatchonly=None, verbose=None):
        return self._call("getwallettransaction", txid, includeWatchonly, verbose)

    def grant(self, addresses, permissions, native_amount=None, startblock=None, endblock=None, comment=None, comment_to=None):
        return self._call("grant", addresses, permissions, native_amount, startblock, endblock, comment, comment_to)

    def grantfrom(self, from_address, to_addresses, permissions, native_amount=None, startblock=None, endblock=None, comment=None, comment_to=None):
        return self._call("grantfrom", from_address, to_addresses, permissions, native_amount, startblock, endblock, comment, comment_to)

    def grantwithdata(self, addresses, permissions, data_or_publish_new_stream_item, native_amount=None, startblock=None, endblock=None):
        return self._call("grantwithdata", addresses, permissions, data_or_publish_new_stream_item, native_amount, startblock, endblock)

    def grantwithdatafrom(self, from_address, to_addresses, permissions, data_or_publish_new_stream_item, native_amount=None, startblock=None, endblock=None):
        return self._call("grantwithdatafrom", from_address, to_addresses, permissions, data_or_publish_new_stream_item, native_amount, startblock, endblock)

    def importaddress(self, addresses, label=None, rescan=None):
        return self._call("importaddress", addresses, label, rescan)

    def importprivkey(self, privkeys, label=None, rescan=None):
        return self._call("importprivkey", privkeys, label, rescan)

    def importwallet(self, filename):
        return self._call("importwallet", filename)

    def issue(self, address, asset_name_or_asset_params, quantity, smallest_unit=None, native_amount=None, custom_fields=None):
        return self._call("issue", address, asset_name_or_asset_params, quantity, smallest_unit, native_amount, custom_fields)

    def issuefrom(self, from_address, to_address, asset_name_or_asset_params, quantity, smallest_unit=None, native_amount=None, custom_fields=None):
        return self._call("issuefrom", from_address, to_address, asset_name_or_asset_params, quantity, smallest_unit, native_amount, custom_fields)

    def issuemore(self, address, asset_identifier, quantity, native_amount=None, custom_fields=None):
        return self._call("issuemore", address, asset_identifier, quantity, native_amount, custom_fields)

    def issuemorefrom(self, from_address, to_address, asset_identifier, quantity, native_amount=None, custom_fields=None):
        return self._call("issuemorefrom", from_address, to_address, asset_identifier, quantity, native_amount, custom_fields)

    def keypoolrefill(self, newsize=None):
        return self._call("keypoolrefill", newsize)

    def listaccounts(self, minconf=None, includeWatchonly=None):
        return self._call("listaccounts", minconf, includeWatchonly)

    def listaddresses(self, addresses=None, verbose=None, count=None, start=None):
        return self._call("listaddresses", addresses, verbose, count, start)

    def listaddressgroupings(self):
        return self._call("listaddressgroupings")

    def listaddresstransactions(self, address, count=None, skip=None, verbose=None):
        return self._call("listaddresstransactions", address, count, skip, verbose)

    def listassettransactions(self, asset_identifier, verbose=None, count=None, start=None, local_ordering=None):
        return self._call("listassettransactions", asset_identifier, verbose, count, start, local_ordering)

    def listlockunspent(self):
        return self._call("listlockunspent")

    def listreceivedbyaccount(self, minconf=None, includeempty=None, includeWatchonly=None):
        return self._call("listreceivedbyaccount", minconf, includeempty, includeWatchonly)

    def listreceivedbyaddress(self, minconf=None, includeempty=None, includeWatchonly=None):
        return self._call("listreceivedbyaddress", minconf, includeempty, includeWatchonly)

    def listsinceblock(self, blockhash=None, target_confirmations=None, includeWatchonly=None):
        return self._call("listsinceblock", blockhash, target_confirmations, includeWatchonly)

    def liststreamblockitems(self, stream_identifier, block_set_identifier, verbose=None, count=None, start=None):
        return self._call("liststreamblockitems", stream_identifier, block_set_identifier, verbose, count, start)

    def liststreamitems(self, stream_identifier, verbose=None, count=None, start=None, local_ordering=None):
        return self._call("liststreamitems", stream_identifier, verbose, count, start, local_ordering)

    def liststreamkeyitems(self, stream_identifier, key, verbose=None, count=None, start=None, local_ordering=None):
        return self._call("liststreamkeyitems", stream_identifier, key, verbose, count, start, local_ordering)

    def liststreamkeys(self, stream_identifier, keys=None, verbose=None, count=None, start=None, local_ordering=None):
        return self._call("liststreamkeys", stream_identifier, keys, verbose, count, start, local_ordering)

    def liststreampublisheritems(self, stream_identifier, address, verbose=None, count=None, start=None, local_ordering=None):
        return self._call("liststreampublisheritems", stream_identifier, address, verbose, count, start, local_ordering)

    def liststreampublishers(self, stream_identifier, addresses=None, verbose=None, count=None, start=None, local_ordering=None):
        return self._call("liststreampublishers", stream_identifier, addresses, verbose, count, start, local_ordering)

    def liststreamtxitems(self, stream_identifier, txid, verbose=None):
        return self._call("liststreamtxitems", stream_identifier, txid, verbose)

    def listtransactions(self, account=None, count=None, from_includeWatchonly=None):
        return self._call("listtransactions", account, count, from_includeWatchonly)

    def listunspent(self, minconf=None, maxconf=None, addresses=None):
        return self._call("listunspent", minconf, maxconf, addresses)

    def listwallettransactions(self, count=None, skip=None, includeWatchonly=None, verbose=None):
        return self._call("listwallettransactions", count, skip, includeWatchonly, verbose)

    def move(self, fromaccount, toaccount, amount, minconf=None, comment=None):
        return self._call("move", fromaccount, toaccount, amount, minconf, comment)

    def preparelockunspent(self, asset_quantities, lock=None):
        return self._call("preparelockunspent", asset_quantities, lock)

    def preparelockunspentfrom(self, from_address, asset_quantities, lock=None):
        return self._call("preparelockunspentfrom", from_address, asset_quantities, lock)

    def publish(self, stream_identifier, key_or_keys, data_hex_or_data_obj):
        return self._call("publish", stream_identifier, key_or_keys, data_hex_or_data_obj)

    def publishfrom(self, from_address, stream_identifier, key_or_keys, data_hex_or_data_obj):
        return self._call("publishfrom", from_address, stream_identifier, key_or_keys, data_hex_or_data_obj)

    def resendwallettransactions(self):
        return self._call("resendwallettransactions")

    def revoke(self, addresses, permissions, native_amount=None, comment=None, comment_to=None):
        return self._call("revoke", addresses, permissions, native_amount, comment, comment_to)

    def revokefrom(self, from_address, to_addresses, permissions, native_amount=None, comment=None, comment_to=None):
        return self._call("revokefrom", from_address, to_addresses, permissions, native_amount, comment, comment_to)

    def send(self, address, amount_or_asset_quantities, comment=None, comment_to=None):
        return self._call("send", address, amount_or_asset_quantities, comment, comment_to)

    def sendasset(self, address, asset_identifier, asset_qty, native_amount=None, comment=None, comment_to=None):
        return self._call("sendasset", address, asset_identifier, asset_qty, native_amount, comment, comment_to)

    def sendassetfrom(self, from_address, to_address, asset_identifier, asset_qty, native_amount=None, comment=None, comment_to=None):
        return self._call("sendassetfrom", from_address, to_address, asset_identifier, asset_qty, native_amount, comment, comment_to)

    def sendfrom(self, from_address, to_address, amount_or_asset_quantities, comment=None, comment_to=None):
        return self._call("sendfrom", from_address, to_address, amount_or_asset_quantities, comment, comment_to)

    def sendfromaccount(self, fromaccount, toaddress, amount, minconf=None, comment=None, comment_to=None):
        return self._call("sendfromaccount", fromaccount, toaddress, amount, minconf, comment, comment_to)

    def sendwithdata(self, address, amount_or_asset_quantities, data_or_publish_new_stream_item):
        return self._call("sendwithdata", address, amount_or_asset_quantities, data_or_publish_new_stream_item)

    def sendwithdatafrom(self, from_address, to_address, amount_or_asset_quantities, data_or_publish_new_stream_item):
        return self._call("sendwithdatafrom", from_address, to_address, amount_or_asset_quantities, data_or_publish_new_stream_item)

    def setaccount(self, address, account):
        return self._call("setaccount", address, account)

    def settxfee(self, amount):
        return self._call("settxfee", amount)

    def signmessage(self, address_or_privkey, message):
        return self._call("signmessage", address_or_privkey, message)

    def subscribe(self, entity_identifiers, rescan=None):
        return self._call("subscribe", entity_identifiers, rescan)

    def unsubscribe(self, entity_identifiers):
        return self._call("unsubscribe", entity_identifiers)

