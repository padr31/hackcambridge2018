export class PResponse {

    time:number;
    interest:number;
    duration:number;
    ts: Array<number>;
    is: Array<number>;
    ds: Array<number>;
    isa: Array<number>;
    status: string;
    status_color: string;
    histogram: Array<number>;
    histogram_labels: Array<string>;

    constructor(time:number, interest:number, duration:number, ts: Array<number>, is: Array<number>, ds: Array<number>, isa: Array<number>,
                status:string, status_color:string, histogram: Array<number>, histogram_labels: Array<string>){
        this.time = time;
        this.interest = interest;
        this.duration = duration;
        this.ts = ts;
        this.is = is;
        this.ds = ds;
        this.isa = isa;
        this.status = status;
        this.status_color = status_color;
        this.histogram = histogram;
        this.histogram_labels = histogram_labels;
    }
}
