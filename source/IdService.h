#ifndef __BLE_ID_SERVICE_H__
#define __BLE_ID_SERVICE_H__

class IdService {
public:
    const static uint16_t ID_SERVICE_UUID              = 0xB000;
    const static uint16_t constexpr ID_STATE_CHARACTERISTIC_UUIDs[] = {0xB001, 0xB002, 0xB003};

    IdService(BLE &_ble, char id1[], char id2[], char id3[]) :
        ble(_ble),
        idNumber1(ID_STATE_CHARACTERISTIC_UUIDs[0], id1),
        idNumber2(ID_STATE_CHARACTERISTIC_UUIDs[1], id2),
        idNumber3(ID_STATE_CHARACTERISTIC_UUIDs[2], id3)
    {
        GattCharacteristic *charTable[] = {&idNumber1, &idNumber2, &idNumber3};
        GattService         idService(IdService::ID_SERVICE_UUID, charTable, sizeof(charTable) / sizeof(GattCharacteristic *));
        ble.gattServer().addService(idService);
    }

private:
    BLE                              &ble;
    ReadOnlyArrayGattCharacteristic<char, 9>  idNumber1;
    ReadOnlyArrayGattCharacteristic<char, 9>  idNumber2;
    ReadOnlyArrayGattCharacteristic<char, 9>  idNumber3;
};

#endif